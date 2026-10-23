import uuid
from sqlalchemy import select
from database.connection import SessionLocal
from models.health_center import HealthCenter
from models.professional import Professional
from models.professional_patient import ProfessionalPatient


def get_health_center(health_center_id: str):
    db = SessionLocal()
    try:
        statement = select(HealthCenter).where(
            HealthCenter.id == health_center_id
        )
        return db.execute(
            statement
        ).scalar_one_or_none()

    finally:
        db.close()

def list_health_centers():
    db = SessionLocal()
    try:
        statement = select(HealthCenter)
        return db.execute(statement).scalars().all()
    finally:
        db.close()

def create_health_center(name: str, city: str):
    db = SessionLocal()
    try:
        health_center = HealthCenter(
            id=str(uuid.uuid4()),
            name=name,
            city=city,
        )

        db.add(health_center)
        db.commit()
        db.refresh(health_center)
        return health_center

    finally:
        db.close()

def update_health_center(health_center_id: str, **fields):
    db = SessionLocal()
    try:
        statement = select(HealthCenter).where(HealthCenter.id == health_center_id)

        health_center = db.execute(statement).scalar_one_or_none()

        if health_center is None:
            return None

        cleaned_fields = {}
        for key, value in fields.items():
            if value is not None:
                cleaned_fields[key] = value

        for field, value in cleaned_fields.items():
            if hasattr(health_center, field):
                setattr(health_center, field, value)

        db.commit()
        db.refresh(health_center)
        return health_center

    finally:
        db.close()

def delete_health_center(health_center_id: str):
    db = SessionLocal()
    try:
        statement = select(HealthCenter).where(HealthCenter.id == health_center_id)
        health_center = db.execute(statement).scalar_one_or_none()

        if health_center is None:
            return None

        prof_statement = select(Professional).where(Professional.health_center_id == health_center_id)
        professionals = db.execute(prof_statement).scalars().all()

        for prof in professionals:
            rel_statement = select(ProfessionalPatient).where(ProfessionalPatient.professional_id == prof.id)
            relations = db.execute(rel_statement).scalars().all()
            for rel in relations:
                db.delete(rel)
            
            db.delete(prof)

        db.delete(health_center)
        db.commit()
        return health_center

    finally:
        db.close()