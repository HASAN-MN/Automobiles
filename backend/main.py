from fastapi import FastAPI
from api.routes import router
from database.config import create_database

app = FastAPI()

# Include the API router
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Automobile Market Analysis API"}