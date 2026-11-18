from sqlalchemy import (
    BigInteger,
    ForeignKey,
    Identity,
    Text
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

from app.database import Base

if TYPE_CHECKING:
    from app.models.repair_request import RepairRequest


class RepairImage(Base):

    __tablename__ = "repair_images"

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

    image_url: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    repair_request: Mapped["RepairRequest"] = relationship(
        back_populates="images"
    )