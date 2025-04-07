import subprocess
import streamlit as st
import pandas as pd
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.config import DATABASE_URL
from ml.model import AutomobileML

FASTAPI_URL = "http://localhost:8000/search"

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
    
    request_payload = {
        "year": year,
        "make": make,
        "model": model,
        "mileage": mileage if mileage > 0 else None
    }

    try:
        response = requests.post(FASTAPI_URL, json=request_payload)
        
        if response.status_code == 200:
            data = response.json()

            avg_price = data.get("average_price", 0)
            vehicles = data.get("listings", [])

            if not vehicles:
                st.warning("No vehicles found for the given criteria.")
            else:
                st.success(f"Estimated Average Market Price: ${avg_price:.2f}")

                sample_listings = pd.DataFrame([
                    {
                        "Make": vehicle['make'],
                        "Model": vehicle['model'],
                        "Price": f"${vehicle['listing_price']:.2f}" if vehicle['listing_price'] else "N/A",
                        "Mileage": f"{vehicle['listing_mileage']:.0f} miles" if vehicle['listing_mileage'] else "N/A",
                        "Location": f"{vehicle['dealer_city']}, {vehicle['dealer_state']}"
                    }
                    for vehicle in vehicles[:100]
                ])
                st.write("### Sample Listings")
                st.table(sample_listings)
        else:
            st.error("Failed to fetch data from FastAPI backend.")
    
    except Exception as e:
        st.error(f"Error while connecting to the backend: {e}")

if st.sidebar.button("Result"):
    st.write("### Data Analysis and Predictions")

    try:
        automobile_ml = AutomobileML()
        automobile_ml.train_and_evaluate()

        st.success("Data Analysis Completed. Check the console for graphs and metrics.")
    except Exception as e:
        st.error(f"Error in ML analysis: {e}")
