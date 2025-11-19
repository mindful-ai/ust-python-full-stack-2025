from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# In-memory "database"
# -----------------------
users = []
incidents = []
customers = [
    {"id": 1, "name": "Alice", "email": "alice@mail.com"},
    {"id": 2, "name": "Bob", "email": "bob@mail.com"},
]

ALLOWED_CITIES = ["Trivandrum", "Bangalore", "Hyderabad", "Chennai"]
ALLOWED_CATEGORIES = ["EMS", "Traffic", "Fire", "Other"]


# -----------------------
# Auth
# -----------------------
@app.post("/register")
def register(data: dict):
    if any(u["username"] == data["username"] for u in users):
        raise HTTPException(400, "User already exists")
    users.append(data)
    return {"msg": "registered"}


@app.post("/login")
def login(data: dict):
    for u in users:
        if u["username"] == data["username"] and u["password"] == data["password"]:
            return {"token": "validtoken", "username": u["username"]}
    raise HTTPException(401, "Invalid credentials")


# -----------------------
# Incidents
# -----------------------
@app.get("/incidents")
def get_incidents():
    return incidents


@app.post("/incidents")
def add_incident(data: dict):

    print(data)

    # Validate city
    if data.get("city") not in ALLOWED_CITIES:
        raise HTTPException(400, "City must be one of: Trivandrum, Bangalore, Hyderabad, Chennai")

    # Validate category
    if data.get("type") not in ALLOWED_CATEGORIES:
        raise HTTPException(400, "Category must be one of: EMS, Traffic, Fire, Other")

    data["id"] = len(incidents) + 1
    incidents.append(data)
    return {"msg": "incident added"}


# -----------------------
# Customers
# -----------------------
@app.get("/customers")
def get_customers():
    return customers


# -----------------------
# Chart Data (updated to reflect incidents)
# -----------------------
@app.get("/chart-data")
def chart_data():
    # Count incidents by city
    city_counts = {city: 0 for city in ALLOWED_CITIES}
    for inc in incidents:
        city_counts[inc["city"]] += 1

    return {
        "cities": list(city_counts.keys()),
        "values": list(city_counts.values())
    }


"""
Run:
uvicorn main:app --reload --port 8000
"""
