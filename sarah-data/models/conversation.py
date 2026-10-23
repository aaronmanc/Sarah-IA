from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from database.connection import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
    )

    created_at: Mapped[str] = mapped_column(
        DateTime,
        nullable=False,
    )