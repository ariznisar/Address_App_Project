# Address Book API

A simple yet powerful RESTful API built with **FastAPI** to manage addresses with geolocation support.  
Users can create, read, update, and delete addresses, and find all addresses within a specified distance from a given location using the Haversine formula.

## Features

- **CRUD operations** for addresses (Create, Read, Update, Delete)
- Geolocation support with **latitude** and **longitude**
- Input validation (latitude -90 to 90, longitude -180 to 180)
- **Nearby search** — find addresses within a given radius (in kilometers)
- SQLite database for persistence (no external DB required)
- Automatic interactive documentation with **Swagger UI** and **ReDoc**

## Tech Stack

- **FastAPI** – modern, fast web framework for building APIs
- **SQLAlchemy** – SQL toolkit and ORM
- **Pydantic** – data validation and settings management
- **SQLite** – lightweight file-based database
- **Haversine formula** – for accurate great-circle distance calculation

## Project Structure

Address-App-Project/
├── app/
│   ├── init.py
│   ├── main.py               # FastAPI app entry point
│   ├── db.py           # DB engine, session & dependency
│   ├── models/
│   │   └── address.py        # SQLAlchemy model
│   ├── schemas/
│   │   └── address.py        # Pydantic schemas (validation)
│   ├── crud/
│   │   └── address.py        # Business logic & distance calculation
│   └── routers/
│       └── addresses.py      # API endpoints
├── .gitignore
├── requirements.txt
└── README.md


## Installation & Setup

1. **Clone the repository**
   git clone git@github.com:ariznisar/Address_App_Project.git
   cd Address_App_Project
2. **Create virtual environment**
   python -m venv venv
   venv\Scripts\activate
3. **Install dependencies**
   pip install -r requirements.txt
4. **Run your Application**
   uvicorn app.main:app --reload


URL for API:
http://127.0.0.1:8000 Interactive docs:
http://127.0.0.1:8000/docs (Swagger UI)
http://127.0.0.1:8000/redoc (ReDoc)