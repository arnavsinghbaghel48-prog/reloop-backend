from sqlalchemy import (
    BigInteger,
    Integer,
    Numeric,
    String,
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


class Application(Base):

    __tablename__ = "applications"

    __table_args__ = (
        UniqueConstraint(
            "repair_request_id",
            "provider_id",
            name="uq_application_request_provider"
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

    proposed_price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    estimated_days: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="pending",
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    repair_request: Mapped["RepairRequest"] = relationship(
        back_populates="applications"
    )

    provider: Mapped["Provider"] = relationship(
        back_populates="applications"
    )