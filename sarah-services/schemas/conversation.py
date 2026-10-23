from datetime import datetime
from pydantic import BaseModel

class Conversation(BaseModel):
    id: str
    created_at: datetime

class CreateConversation(BaseModel):
    created_at: datetime | None = None
