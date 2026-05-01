from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from enum import Enum
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


class LostItemStatus(str, Enum):
    OPEN = "open"
    LOCKED = "locked"
    CLAIMED = "claimed"
    CLOSED = "closed"


class LostItemBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str = Field(min_length=1, max_length=1000)
    reward: Decimal = Field(gt=0)
    owner_oib: str = Field(min_length=11, max_length=11, pattern=r"^\d{11}$")
    status: LostItemStatus = LostItemStatus.OPEN
    wallet_address: str | None = Field(default=None, min_length=1, max_length=128)
    blockchain_hash: str | None = Field(default=None, min_length=1, max_length=128)

    @field_validator("title", "description")
    @classmethod
    def strip_text(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("field must not be empty")
        return cleaned


class LostItemCreate(LostItemBase):
    pass


class LostItemRead(LostItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.utcnow)


class LostItemRecord(LostItemRead):
    pass


class BountyClaim(BaseModel):
    claimant_name: str = Field(min_length=1, max_length=200)
    proof_hash: str = Field(min_length=1, max_length=128)

    @field_validator("claimant_name", "proof_hash")
    @classmethod
    def strip_claim_fields(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("field must not be empty")
        return cleaned
