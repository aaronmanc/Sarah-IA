import uuid
from datetime import datetime
from sqlalchemy import select
from database.connection import SessionLocal
from models.message import Message
from models.image import Image
from models.sarah_version import SarahVersion

def get_message(message_id: str):
    db = SessionLocal()
    try:
        statement = select(Message).where(Message.id == message_id)
        return db.execute(statement).scalar_one_or_none()
    finally:
        db.close()

def list_messages():
    db = SessionLocal()
    try:
        statement = select(Message)
        return db.execute(statement).scalars().all()
    finally:
        db.close()

def create_message(
    conversation_id: str,
    sender_type: str,
    sender_id: str,
    content: str,
    created_at: datetime | None = None,
    image_id: str | None = None,
    patient_id: str | None = None,
    professional_id: str | None = None,
    sarah_version_id: str | None = None,
):
    db = SessionLocal()
    try:
        message = Message(
            id=str(uuid.uuid4()),
            conversation_id=conversation_id,
            sender_type=sender_type,
            sender_id=sender_id,
            content=content,
            created_at=created_at or datetime.now(),
            image_id = image_id,
            patient_id=patient_id,
            professional_id=professional_id,
            sarah_version_id=sarah_version_id,
        )
        db.add(message)
        db.commit()
        db.refresh(message)
        return message
    finally:
        db.close()

    
def update_message(
    message_id: str,
    content: str | None = None,
    sender_type: str | None = None,
    sender_id: str | None = None,
    image_id: str | None = None,
):
    db = SessionLocal()
    try:
        statement = select(Message).where(Message.id == message_id)
        message = db.execute(statement).scalar_one_or_none()

        if message is None:
            return None
        if content is not None:
            message.content = content
        if sender_type is not None:
            message.sender_type = sender_type
        if sender_id is not None:
            message.sender_id = sender_id
        if image_id is not None:
            message.image_id = image_id

        db.commit()
        db.refresh(message)
        return message
    finally:
        db.close()