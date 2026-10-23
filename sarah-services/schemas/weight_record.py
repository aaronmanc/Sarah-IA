from pydantic import BaseModel
from datetime import datetime

class WeightRecord(BaseModel):
    id: str
    weight: float
    recorded_at: datetime
    patient_id: str

class CreateWeightRecord(BaseModel):
    weight: float
    recorded_at: datetime | None = None
    patient_id: str

class UpdateWeightRecord(BaseModel):
    weight: float | None = None
    recorded_at: datetime | None = None