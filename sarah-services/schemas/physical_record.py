from pydantic import BaseModel
from datetime import datetime

class PhysicalActivityRecord(BaseModel):
    id: str
    activity_type: str
    duration: float
    recorded_at: datetime
    patient_id: str

class CreatePhysicalActivityRecord(BaseModel):
    activity_type: str
    duration: float
    recorded_at: datetime | None = None
    patient_id: str

class UpdatePhysicalActivityRecord(BaseModel):
    activity_type: str | None = None
    duration: float | None = None
    recorded_at: datetime | None = None