import uuid
from datetime import datetime
from sqlalchemy import select
from database.connection import SessionLocal
from models.weight_record import WeightRecord


def get_weight_record(record_id: str):
    db = SessionLocal()
    try:
        statement = select(WeightRecord).where(WeightRecord.id == record_id)
        return db.execute(statement).scalar_one_or_none()
    finally:
        db.close()


def create_weight_record(
    weight: float,
    patient_id: str,
    recorded_at: datetime | None = None,
):
    db = SessionLocal()
    try:
        record = WeightRecord(
            id=str(uuid.uuid4()),
            weight=weight,
            patient_id=patient_id,
            recorded_at=recorded_at or datetime.now(),
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return record
    finally:
        db.close()


def update_weight_record(record_id: str, **fields):
    db = SessionLocal()
    try:
        statement = select(WeightRecord).where(WeightRecord.id == record_id)
        record = db.execute(statement).scalar_one_or_none()

        if record is None:
            return None

        for field, value in fields.items():
            if hasattr(record, field):
                setattr(record, field, value)

        db.commit()
        db.refresh(record)
        return record
    finally:
        db.close()


def delete_weight_record(record_id: str):
    db = SessionLocal()
    try:
        statement = select(WeightRecord).where(WeightRecord.id == record_id)
        record = db.execute(statement).scalar_one_or_none()

        if record is None:
            return None

        db.delete(record)
        db.commit()
        return record
    finally:
        db.close()

        