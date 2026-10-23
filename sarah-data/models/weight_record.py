from datetime import datetime
from sqlalchemy import String, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base


class WeightRecord(Base):
    __tablename__ = "weight_records"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    weight: Mapped[float] = mapped_column(
        Float,
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