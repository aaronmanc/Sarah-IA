from datetime import datetime
from sqlalchemy import String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base


class FoodRecord(Base):
    __tablename__ = "food_records"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    recorded_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    patient_id: Mapped[str] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False,
    )