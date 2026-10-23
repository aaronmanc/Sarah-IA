import uuid
from sqlalchemy import select
from database.connection import SessionLocal
from models.professional import Professional
from models.health_center import HealthCenter


def get_professional(
    professional_id: str,
):
    db = SessionLocal()
    try:
        statement = select(Professional).where(
            Professional.id == professional_id
        )
        return db.execute(
            statement
        ).scalar_one_or_none()

    finally:
        db.close()

def list_professionals():
    db = SessionLocal()
    try:
        statement = select(Professional)
        return db.execute(statement).scalars().all()
    finally:
        db.close()


def create_professional(
    first_name: str,
    last_name: str,
    specialty: str,
    email: str,
    phone: str,
    health_center_id: str,
):
    db = SessionLocal()
    try:
        health_center = db.execute(
            select(HealthCenter).where(
                HealthCenter.id == health_center_id
            )
        ).scalar_one_or_none()

        if health_center is None:
            return None

        professional = Professional(
            id=str(uuid.uuid4()),
            first_name=first_name,
            last_name=last_name,
            specialty=specialty,
            email=email,
            phone=phone,
            health_center_id=health_center_id,
        )

        db.add(professional)
        db.commit()
        db.refresh(professional)
        return professional

    finally:
        db.close()


def update_professional(
    professional_id: str,
    **fields,
):
    db = SessionLocal()
    try:
        statement = select(Professional).where(
            Professional.id == professional_id
        )

        professional = db.execute(
            statement
        ).scalar_one_or_none()

        if professional is None:
            return None
        
        if "health_center_id" in fields:
            health_center = db.execute(
                select(HealthCenter).where(
                    HealthCenter.id == fields["health_center_id"]
                )
            ).scalar_one_or_none()

            if health_center is None:
                return None

        for field, value in fields.items():
            if hasattr(professional, field):
                setattr(
                    professional,
                    field,
                    value,
                )

        db.commit()
        db.refresh(professional)
        return professional

    finally:
        db.close()


def delete_professional(
    professional_id: str,
):
    db = SessionLocal()
    try:
        statement = select(Professional).where(
            Professional.id == professional_id
        )

        professional = db.execute(
            statement
        ).scalar_one_or_none()

        if professional is None:
            return None

        db.delete(professional)
        db.commit()
        return professional

    finally:
        db.close()

        