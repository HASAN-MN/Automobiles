from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.config import get_db
from database.crud import get_vehicle_listings_by_criteria, calculate_average_price
from schemas.response import VehicleSearchResponse
from schemas.request import VehicleSearchRequest

router = APIRouter()

# Search endpoint
@router.post("/search", response_model=VehicleSearchResponse)
def search_vehicles(request: VehicleSearchRequest, db: Session = Depends(get_db)):
    vehicles = get_vehicle_listings_by_criteria(db, year=request.year, make=request.make, model=request.model)
    average_price = calculate_average_price(vehicles, mileage=request.mileage)

    return {
        "average_price": average_price,
        "listings": vehicles[:100]  # Limit response to 100 listings
    }
