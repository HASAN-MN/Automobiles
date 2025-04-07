import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from backend.data_preprocess import preprocess_txt_file
from database.config import DATABASE_URL, SessionLocal
from database.crud import get_vehicle_listings_by_criteria, calculate_average_price
from ml.model import AutomobileML

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

st.title("Automobile Market Analysis")

year = st.sidebar.number_input("Year", min_value=1900, max_value=2050, value=2015, step=1)
make = st.sidebar.text_input("Make", value="Toyota")
model = st.sidebar.text_input("Model", value="Camry")
mileage = st.sidebar.number_input("Mileage (optional)", min_value=0, value=0, step=100)

if st.sidebar.button("Preprocess TXT File"):
    try:
        result = subprocess.run(["python", "Backend/data_preprocess.py"], capture_output=True, text=True)
        st.success("TXT file processed and data stored in MySQL database.")
        st.text(result.stdout)
    except Exception as e:
        st.error(f"Error while processing TXT file: {e}")

if st.sidebar.button("Search"):
    st.write("### Vehicle Listings and Market Price")

    db = SessionLocal()
    try:
        # Fetch vehicle listings
        vehicles = get_vehicle_listings_by_criteria(db, year=year, make=make, model=model)
        avg_price = calculate_average_price(vehicles, mileage=mileage)

        if not vehicles:
            st.warning("No vehicles found for the given criteria.")
        else:
            st.success(f"Estimated Average Market Price: ${avg_price:.2f}")
            
            # Display sample listings
            sample_listings = pd.DataFrame([
                {
                    "Make": vehicle.make,
                    "Model": vehicle.model,
                    "Price": f"${vehicle.listing_price:.2f}",
                    "Mileage": f"{vehicle.listing_mileage:.0f} miles" if vehicle.listing_mileage else "N/A",
                    "Location": f"{vehicle.dealer_city}, {vehicle.dealer_state}"
                }
                for vehicle in vehicles[:100]
            ])
            st.write("### Sample Listings")
            st.table(sample_listings)
    finally:
        db.close()


if st.sidebar.button("Result"):
    st.write("### Data Analysis and Predictions")

    try:
        # Train and evaluate ML models
        automobile_ml = AutomobileML()
        automobile_ml.train_and_evaluate()

        st.success("Data Analysis Completed. Check the console for graphs and metrics.")
    except Exception as e:
        st.error(f"Error in ML analysis: {e}")
