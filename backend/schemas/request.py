from pydantic import BaseModel
from typing import Optional, List

class VehicleSearchRequest(BaseModel):
    year: int
    make: str
    model: str
    mileage: Optional[float]