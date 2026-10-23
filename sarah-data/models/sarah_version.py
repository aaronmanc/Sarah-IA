from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base


class SarahVersion(Base):
    __tablename__ = "sarah_versions"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    nombre: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )