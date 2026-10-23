from sqlalchemy import String, ForeignKey, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    conversation_id: Mapped[str] = mapped_column(
        ForeignKey("conversations.id"),
        nullable=False,
    )

    sender_type: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    sender_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        DateTime,
        nullable=False,
    )

    image_id: Mapped[str] = mapped_column(
        ForeignKey("images.id"),
        nullable=True,
    )

    patient_id: Mapped[str | None] = mapped_column(
        ForeignKey("patients.id"),
        nullable=True,
    )

    professional_id: Mapped[str | None] = mapped_column(
        ForeignKey("professionals.id"),
        nullable=True,
    )

    sarah_version_id: Mapped[str | None] = mapped_column(
        ForeignKey("sarah_versions.id"),
        nullable=False,
    )