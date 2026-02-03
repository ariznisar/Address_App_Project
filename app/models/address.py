from sqlalchemy import Column, Integer, String, Float
from app.db import Base


class AddressDB(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    zip_code = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)