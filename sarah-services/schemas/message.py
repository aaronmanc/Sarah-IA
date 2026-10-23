from datetime import datetime
from pydantic import BaseModel

class Message(BaseModel):
    id: str
    conversation_id: str
    sender_type: str
    sender_id: str
    content: str
    created_at: datetime
    image_id: str | None = None
    patient_id: str | None = None
    professional_id: str | None = None
    sarah_version_id: str

class CreateMessage(BaseModel):
    conversation_id: str
    sender_type: str
    sender_id: str
    content: str
    created_at: datetime | None = None
    image_id: str | None = None
    patient_id: str | None = None
    professional_id: str | None = None
    sarah_version_id: str

class UpdateMessage(BaseModel):
    sender_type: str | None = None
    sender_id: str | None = None
    content: str | None = None
    image_id: str | None = None