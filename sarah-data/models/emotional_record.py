from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base


class EmotionalRecord(Base):
    __tablename__ = "emotional_records"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    emotional_state: Mapped[str] = mapped_column(
        String,
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