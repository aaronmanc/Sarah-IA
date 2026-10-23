from datetime import datetime
from pydantic import BaseModel

class EmotionalRecord(BaseModel):
    id: str
    emotional_state: str
    recorded_at: datetime
    patient_id: str

class CreateEmotionalRecord(BaseModel):
    emotional_state: str
    recorded_at: datetime | None = None
    patient_id: str

class UpdateEmotionalRecord(BaseModel):
    emotional_state: str | None = None
    recorded_at: datetime | None = None