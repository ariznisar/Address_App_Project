from pydantic import BaseModel, field_validator
from typing import Optional


class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    latitude: float
    longitude: float

    @field_validator('latitude')
    @classmethod
    def validate_latitude(cls, v: float) -> float:
        if not -90 <= v <= 90:
            raise ValueError('Latitude must be between -90 and 90')
        return v

    @field_validator('longitude')
    @classmethod
    def validate_longitude(cls, v: float) -> float:
        if not -180 <= v <= 180:
            raise ValueError('Longitude must be between -180 and 180')
        return v


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    @field_validator('latitude')
    @classmethod
    def validate_latitude(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and not -90 <= v <= 90:
            raise ValueError('Latitude must be between -90 and 90')
        return v

    @field_validator('longitude')
    @classmethod
    def validate_longitude(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and not -180 <= v <= 180:
            raise ValueError('Longitude must be between -180 and 180')
        return v


class Address(AddressBase):
    id: int

    class Config:
        from_attributes = True