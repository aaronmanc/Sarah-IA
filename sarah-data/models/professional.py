from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base


class Professional(Base):
    __tablename__ = "professionals"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    first_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    last_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    specialty: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    health_center_id: Mapped[str] = mapped_column (
        ForeignKey("health_centers.id"),
        nullable=False,
    )