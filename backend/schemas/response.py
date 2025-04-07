from pydantic import BaseModel
from typing import Optional, List

class VehicleListingResponse(BaseModel):
    vin: str
    year: int
    make: str
    model: str
    trim: Optional[str]
    dealer_name: str
    dealer_city: str
    dealer_state: str
    listing_price: Optional[float]
    listing_mileage: Optional[float]
    used: bool
    certified: bool
    style: Optional[str]
    driven_wheels: Optional[str]
    fuel_type: Optional[str]
    exterior_color: Optional[str]
    interior_color: Optional[str]
    listing_status: Optional[str]

class VehicleSearchResponse(BaseModel):
    average_price: Optional[float]
    listings: List[VehicleListingResponse]