import uuid
from datetime import datetime
from sqlalchemy import select, delete
from database.connection import SessionLocal
from models.conversation import Conversation
from models.message import Message


def get_conversation(conversation_id: str):
    db = SessionLocal()
    try:
        statement = select(Conversation).where(Conversation.id == conversation_id)
        return db.execute(statement).scalar_one_or_none()
    finally:
        db.close()

def list_conversations():
    db = SessionLocal()
    try:
        statement = select(Conversation)
        return db.execute(statement).scalars().all()
    finally:
        db.close()

def create_conversation(created_at: datetime | None = None):
    db = SessionLocal()
    try:
        conversation = Conversation(
            id=str(uuid.uuid4()),
            created_at = created_at or datetime.now(),
        )
        db.add(conversation)
        db.commit()
        db.refresh(conversation)
        return conversation
    finally:
        db.close()


def delete_conversation(conversation_id: str):
    db = SessionLocal()
    try:
        statement = select(Conversation).where(Conversation.id == conversation_id)
        conversation = db.execute(statement).scalar_one_or_none()

        if conversation is None:
            return None
        
        db.execute(delete(Message).where(Message.conversation_id == conversation_id))

        db.delete(conversation)
        db.commit()
        return conversation
    finally:
        db.close()

        