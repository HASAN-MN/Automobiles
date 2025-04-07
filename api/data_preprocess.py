import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL)

def preprocess_txt_file():
    file_path = "inventory.txt"  # File path for input data
    chunk_size = 100000
    filtered_data = []

    for chunk in pd.read_csv(file_path, delimiter="|", chunksize=chunk_size, low_memory=False):
        chunk['listing_price'] = pd.to_numeric(chunk['listing_price'], errors='coerce').fillna(0)
        filtered_chunk = chunk[
            (chunk['listing_price'] > 20000) & 
            (chunk['driven_wheels'].isin(['FWD', 'AWD']))
        ]
        filtered_data.append(filtered_chunk)

    filtered_df = pd.concat(filtered_data)
    filtered_df.to_csv("filtered_cars.csv", index=False)
    filtered_df.to_sql(name="vehicles", con=engine, index=False, if_exists="replace")

    print("Preprocessing completed and data stored in the MySQL database.")

if __name__ == "__main__":
    preprocess_txt_file()
