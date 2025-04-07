import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)

def load_data():
    query = "SELECT year, make, model, listing_price, listing_mileage FROM vehicles WHERE listing_price IS NOT NULL"
    data = pd.read_sql(query, con=engine)
    return data

def preprocess_data(data):
    data = data.dropna(subset=["listing_price", "listing_mileage"])
    data = pd.get_dummies(data, columns=["make", "model"], drop_first=True)
    X = data.drop(columns=["listing_price"])
    y = data["listing_price"]

    return X, y
