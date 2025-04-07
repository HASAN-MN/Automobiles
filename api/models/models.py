from sqlalchemy import Column, Integer, String, Float, Boolean, Date, Text
from database.config import Base

class VehicleListing(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String(17), index=True)
    year = Column(Integer, index=True)
    make = Column(String(50), index=True)
    model = Column(String(50), index=True)
    trim = Column(String(100), nullable=True)
    dealer_name = Column(String(100))
    dealer_street = Column(String(100))
    dealer_city = Column(String(50))
    dealer_state = Column(String(2))
    dealer_zip = Column(String(10))
    listing_price = Column(Float, nullable=True)
    listing_mileage = Column(Float, nullable=True)
    used = Column(Boolean)
    certified = Column(Boolean)
    style = Column(String(100), nullable=True)
    driven_wheels = Column(String(50), nullable=True)
    engine = Column(String(50), nullable=True)
    fuel_type = Column(String(50), nullable=True)
    exterior_color = Column(String(50), nullable=True)
    interior_color = Column(String(50), nullable=True)
    seller_website = Column(Text, nullable=True)
    first_seen_date = Column(Date)
    last_seen_date = Column(Date)
    dealer_vdp_last_seen_date = Column(Date, nullable=True)
    listing_status = Column(String(50), nullable=True)
