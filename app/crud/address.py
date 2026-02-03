from sqlalchemy.orm import Session
import math
from app.models.address import AddressDB
from app.schemas.address import AddressCreate, AddressUpdate


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


def create_address(db: Session, address: AddressCreate) -> AddressDB:
    db_address = AddressDB(**address.model_dump())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def get_address(db: Session, address_id: int) -> AddressDB | None:
    return db.query(AddressDB).filter(AddressDB.id == address_id).first()


def update_address(db: Session, address_id: int, address_update: AddressUpdate) -> AddressDB | None:
    db_address = get_address(db, address_id)
    if not db_address:
        return None

    update_data = address_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_address, key, value)

    db.commit()
    db.refresh(db_address)
    return db_address


def delete_address(db: Session, address_id: int) -> bool:
    db_address = get_address(db, address_id)
    if not db_address:
        return False
    db.delete(db_address)
    db.commit()
    return True


def get_nearby_addresses(db: Session, lat: float, lon: float, distance_km: float) -> list[AddressDB]:
    all_addresses = db.query(AddressDB).all()
    nearby = [
        addr for addr in all_addresses
        if haversine(lat, lon, addr.latitude, addr.longitude) <= distance_km
    ]
    return nearby