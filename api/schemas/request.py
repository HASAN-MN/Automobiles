from pydantic import BaseModel
from typing import Optional

class VehicleSearchRequest(BaseModel):
    year: int
    make: str
    model: str
    mileage: Optional[float]