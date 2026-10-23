from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base


class HealthCenter(Base):
    __tablename__ = "health_centers"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )