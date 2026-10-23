import uuid
from sqlalchemy import select
from database.connection import SessionLocal
from models.image import Image

def get_image(image_id: str):
    db = SessionLocal()
    try:
        statement = select(Image).where(Image.id == image_id)
        return db.execute(statement).scalar_one_or_none()
    finally:
        db.close()

def create_image(description: str, image_type: str, file_reference: str):
    db = SessionLocal()
    try:
        image = Image(
            id=str(uuid.uuid4()),
            description=description,
            image_type=image_type,
            file_reference=file_reference,
        )
        
        db.add(image)
        db.commit()
        db.refresh(image)
        return image
    finally:
        db.close()

def delete_image(image_id: str):
    db = SessionLocal()
    try:
        statement = select(Image).where(Image.id == image_id)
        image = db.execute(statement).scalar_one_or_none()

        if image is None:
            return None

        db.delete(image)
        db.commit()
        return image
    finally:
        db.close()

        