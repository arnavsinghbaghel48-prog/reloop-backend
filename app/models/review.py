from sqlalchemy import (
    BigInteger,
    Integer,
    Text,
    ForeignKey,
    Identity,
    DateTime,
    func,
    UniqueConstraint
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.database import Base

if TYPE_CHECKING:
    from app.models.repair_request import RepairRequest
    from app.models.provider import Provider


class Review(Base):
    __tablename__ = "reviews"

    __table_args__ = (
        UniqueConstraint(
            "repair_request_id",
            name="uq_review_repair_request"
        ),
    )

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True
    )

    repair_request_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("repair_requests.id", ondelete="CASCADE"),
        nullable=False
    )

    provider_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("providers.id", ondelete="CASCADE"),
        nullable=False
    )

    rating: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    comment: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    repair_request: Mapped["RepairRequest"] = relationship(
        back_populates="review"
    )

    provider: Mapped["Provider"] = relationship(
        back_populates="reviews"
    )