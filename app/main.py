from fastapi import FastAPI
from app.routers import addresses
from app.db import engine
from app.models.address import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Address Book API",
    description="API to manage addresses with geolocation support",
    version="1.0.0"
)

app.include_router(addresses.router, prefix="/addresses", tags=["addresses"])

## list of commands on how to run the app

# cd Address_App_Project (create directory for project and inside the project all commands below)
# create virtual environment and activate  it (e.g venv)
# pip install -r requirements.txt (Install dependencies listed in requirements.txt file)
# uvicorn app.main:app --reload (command to run app)