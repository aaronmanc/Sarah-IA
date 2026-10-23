from sqlalchemy import select
from database.connection import SessionLocal
from models.professional_patient import ProfessionalPatient


def get_professional_patient(professional_id: str,patient_id: str,):
    db = SessionLocal()
    try:
        statement = select(ProfessionalPatient).where(
            ProfessionalPatient.professional_id == professional_id,
            ProfessionalPatient.patient_id == patient_id,
        )
        return db.execute(
            statement
        ).scalar_one_or_none()

    finally:
        db.close()

def list_professional_patients():
    db = SessionLocal()
    try:
        statement = select(ProfessionalPatient)
        return db.execute(statement).scalars().all()
    finally:
        db.close()

def create_professional_patient(professional_id: str, patient_id: str,):
    db = SessionLocal()
    try:
        relation = ProfessionalPatient(
            professional_id=professional_id,
            patient_id=patient_id,
        )

        db.add(relation)
        db.commit()
        db.refresh(relation)
        return relation

    finally:
        db.close()


def update_professional_patient(professional_id: str, patient_id: str, **fields):
    db = SessionLocal()
    try:
        statement = select(ProfessionalPatient).where(
            ProfessionalPatient.professional_id == professional_id,
            ProfessionalPatient.patient_id == patient_id,
        )

        relation = db.execute(
            statement
        ).scalar_one_or_none()

        if relation is None:
            return None

        for field, value in fields.items():
            if hasattr(relation, field):
                setattr(
                    relation,
                    field,
                    value,
                )

        db.commit()
        db.refresh(relation)
        return relation

    finally:
        db.close()


def delete_professional_patient(professional_id: str, patient_id: str):
    db = SessionLocal()
    try:
        statement = select(ProfessionalPatient).where(
            ProfessionalPatient.professional_id == professional_id,
            ProfessionalPatient.patient_id == patient_id,
        )

        relation = db.execute(
            statement
        ).scalar_one_or_none()

        if relation is None:
            return None

        db.delete(relation)
        db.commit()
        return relation

    finally:
        db.close()

        