import uuid
from datetime import datetime
from sqlalchemy import select
from database.connection import SessionLocal
from models.emotional_record import EmotionalRecord


def get_emotional_record(record_id: str):
    db = SessionLocal()
    try:
        statement = select(EmotionalRecord).where(EmotionalRecord.id == record_id)
        return db.execute(statement).scalar_one_or_none()
    finally:
        db.close()

def list_emotional_records(patient_id: str = None):
    db = SessionLocal()
    try:
        statement = select(EmotionalRecord)
        if patient_id:
            statement = statement.where(EmotionalRecord.patient_id == patient_id)
        return db.execute(statement).scalars().all()
    finally:
        db.close()


def create_emotional_record(
    emotional_state: str,
    patient_id: str,
    recorded_at: datetime | None = None,
):
    db = SessionLocal()
    try:
        record = EmotionalRecord(
            id=str(uuid.uuid4()),
            emotional_state=emotional_state,
            patient_id=patient_id,
            recorded_at=recorded_at or datetime.now(),
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return record
    finally:
        db.close()


def update_emotional_record(record_id: str, **fields):
    db = SessionLocal()
    try:
        statement = select(EmotionalRecord).where(EmotionalRecord.id == record_id)
        record = db.execute(statement).scalar_one_or_none()

        if record is None:
            return None

        cleaned_fields = {}
        for key, value in fields.items():
            if value is not None:
                cleaned_fields[key] = value

        for field, value in cleaned_fields.items():
            if hasattr(record, field):
                setattr(record, field, value)

        db.commit()
        db.refresh(record)
        return record
    finally:
        db.close()


def delete_emotional_record(record_id: str):
    db = SessionLocal()
    try:
        statement = select(EmotionalRecord).where(EmotionalRecord.id == record_id)
        record = db.execute(statement).scalar_one_or_none()

        if record is None:
            return None

        db.delete(record)
        db.commit()
        return record
    finally:
        db.close()

        