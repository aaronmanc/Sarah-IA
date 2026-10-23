from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base

class ProfessionalPatient(Base):
    __tablename__ = "professional_patients"

    professional_id: Mapped[str] = mapped_column(
        ForeignKey("professionals.id"),
        primary_key=True,
    )

    patient_id: Mapped[str] = mapped_column(
        ForeignKey("patients.id"),
        primary_key=True,
    )