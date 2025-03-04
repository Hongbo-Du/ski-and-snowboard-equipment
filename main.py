from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define user input schema
class SkiRequest(BaseModel):
    height: int
    weight: int
    level: Literal["beginner", "intermediate", "high-level"]
    location: Literal["resort", "backcountry"]

# Recommendation logic
def recommend_ski_equipment(height: int, weight: int, level: str, location: str):
    # Define basic ski type selection based on location
    if location == "backcountry":
        ski_type = "Backcountry Skis"
    else:
        ski_type = "All Mountain Skis"

    # Ski size estimation based on height
    if height < 160:
        ski_size = "150cm-160cm"
    elif 160 <= height < 175:
        ski_size = "165cm-170cm"
    else:
        ski_size = "175cm-185cm"

    # DIN setting based on weight and level
    if level == "beginner":
        din = "3-4"
    elif level == "intermediate":
        din = "5-7"
    else:
        din = "8-12"

    # Boot size estimation based on weight
    boot_size = 260 if weight < 65 else 270 if weight < 85 else 280

    # Boot flex based on level
    boot_flex = "60-80" if level == "beginner" else "80-100" if level == "intermediate" else "100-120"

    return {
        "ski_type": ski_type,
        "ski_size": ski_size,
        "DIN": din,
        "boot_size": boot_size,
        "boot_flex": boot_flex
    }

# Fix 1: Add a root endpoint
@app.get("/")
def read_root():
    return {"message": "Ski Recommendation API is running"}

# Fix 2: Ensure `/recommend` only accepts `POST`
@app.post("/recommend")
async def get_recommendation(data: SkiRequest):
    return {"recommendation received": recommend_ski_equipment(data.height, data.weight, data.level, data.location)}

