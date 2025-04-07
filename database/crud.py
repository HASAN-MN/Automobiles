from sqlalchemy.orm import Session
from backend.models.models import VehicleListing  # Updated import

# Get vehicle listings by search criteria
def get_vehicle_listings_by_criteria(db: Session, year: int, make: str, model: str):
    return db.query(VehicleListing).filter(
        VehicleListing.year == year,
        VehicleListing.make == make,
        VehicleListing.model == model
    ).all()

# Calculate average price of vehicle listings
def calculate_average_price(vehicles: list, mileage: float = None):
    if not vehicles:
        return None

    total_price = sum(vehicle.listing_price for vehicle in vehicles if vehicle.listing_price is not None)
    count = len([vehicle for vehicle in vehicles if vehicle.listing_price is not None])
    if count == 0:
        return None

    average_price = total_price / count

    if mileage:
        adjustment_factor = 0.05  # Example adjustment factor
        average_price = max(average_price - (mileage * adjustment_factor), 0)

    return round(average_price, -2)
