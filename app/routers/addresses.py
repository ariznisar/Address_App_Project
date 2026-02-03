from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.schemas.address import Address, AddressCreate, AddressUpdate
from app.crud.address import (
    create_address,
    get_address,
    update_address,
    delete_address,
    get_nearby_addresses
)

router = APIRouter()


@router.post("/", response_model=Address, status_code=201)
def create_new_address(address: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db, address)


@router.get("/{address_id}", response_model=Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = get_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@router.put("/{address_id}", response_model=Address)
def update_existing_address(
    address_id: int,
    address: AddressUpdate,
    db: Session = Depends(get_db)
):
    updated = update_address(db, address_id, address)
    if updated is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return updated


@router.delete("/{address_id}")
def remove_address(address_id: int, db: Session = Depends(get_db)):
    success = delete_address(db, address_id)
    if not success:
        raise HTTPException(status_code=404, detail="Address not found")
    return {"detail": "Address deleted successfully"}


@router.get("/nearby/", response_model=List[Address])
def get_addresses_nearby(
    lat: float = Query(..., description="Reference latitude"),
    lon: float = Query(..., description="Reference longitude"),
    distance: float = Query(..., description="Maximum distance in km"),
    db: Session = Depends(get_db)
):
    return get_nearby_addresses(db, lat, lon, distance)