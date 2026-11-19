from sqlalchemy import (
    BigInteger,
    Integer,
    String,
    Text,
    ForeignKey,
    Identity,
    DateTime,
    func
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.application import Application
    from app.models.review import Review


class Provider(Base):

    __tablename__ = "providers"

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    experience_years: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    service_location: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    user: Mapped["User"] = relationship(
    back_populates="provider"
)
    applications: Mapped[list["Application"]] = relationship(
    back_populates="provider",
    cascade="all, delete-orphan"
)
    reviews: Mapped[list["Review"]] = relationship(
    back_populates="provider",
    cascade="all, delete-orphan"
)