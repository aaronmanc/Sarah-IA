from datetime import datetime
from pydantic import BaseModel

class FoodRecord(BaseModel):
    id: str
    description: str
    recorded_at: datetime
    patient_id: str

class CreateFoodRecord(BaseModel):
    description: str
    recorded_at: datetime | None = None
    patient_id: str

class UpdateFoodRecord(BaseModel):
    description: str | None = None
    recorded_at: datetime | None = None