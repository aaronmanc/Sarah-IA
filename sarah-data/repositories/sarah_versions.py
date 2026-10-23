import uuid
from sqlalchemy import select
from database.connection import SessionLocal
from models.sarah_version import SarahVersion


def get_sarah_version(version_id: str):
    db = SessionLocal()
    try:
        statement = select(SarahVersion).where(SarahVersion.id == version_id)
        return db.execute(statement).scalar_one_or_none()
    finally:
        db.close()


def create_sarah_version(nombre: str, description: str):
    db = SessionLocal()
    try:
        sarah_version = SarahVersion(
            id=str(uuid.uuid4()),
            nombre=nombre,
            description=description,
        )
        db.add(sarah_version)
        db.commit()
        db.refresh(sarah_version)
        return sarah_version
    finally:
        db.close()


def update_sarah_version(version_id: str, **fields):
    db = SessionLocal()
    try:
        statement = select(SarahVersion).where(SarahVersion.id == version_id)
        sarah_version = db.execute(statement).scalar_one_or_none()

        if sarah_version is None:
            return None

        for field, value in fields.items():
            if hasattr(sarah_version, field):
                setattr(sarah_version, field, value)

        db.commit()
        db.refresh(sarah_version)
        return sarah_version
    finally:
        db.close()


def delete_sarah_version(version_id: str):
    db = SessionLocal()
    try:
        statement = select(SarahVersion).where(SarahVersion.id == version_id)
        sarah_version = db.execute(statement).scalar_one_or_none()

        if sarah_version is None:
            return None

        db.delete(sarah_version)
        db.commit()
        return sarah_version
    finally:
        db.close()

        