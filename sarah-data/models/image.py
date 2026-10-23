from datetime import date
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base

class Image(Base):
   __tablename__ = "images"

   id: Mapped[str] = mapped_column(
       String,
       primary_key=True,
   )

   file_reference: Mapped[str] = mapped_column(
       String,
       nullable=False,
   )

   image_type: Mapped[str] = mapped_column(
       String,
       nullable=False,
   )

   description: Mapped[str] = mapped_column(
       Text,
       nullable=False,
   )