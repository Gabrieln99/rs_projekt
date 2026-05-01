from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from myapp.core.blockchain import SimulatedBlockchain
from myapp.core.domain import BountyClaim, LostItemCreate, LostItemRecord, LostItemStatus
from myapp.data.repository import BountyRepository


class BountyService:
    def __init__(
        self,
        repository: BountyRepository | None = None,
        blockchain: SimulatedBlockchain | None = None,
    ) -> None:
        self.repository = repository or BountyRepository()
        self.blockchain = blockchain or SimulatedBlockchain()

    def create_bounty(self, payload: LostItemCreate) -> LostItemRecord:
        blockchain_hash = self.blockchain.create_escrow(payload.reward, payload.owner_oib)
        item = LostItemRecord(
            id=str(uuid4()),
            created_at=datetime.utcnow(),
            title=payload.title,
            description=payload.description,
            reward=payload.reward,
            owner_oib=payload.owner_oib,
            status=payload.status if payload.status else LostItemStatus.OPEN,
            wallet_address=payload.wallet_address,
            blockchain_hash=payload.blockchain_hash or blockchain_hash,
        )
        return self.repository.add(item)

    def list_bounties(self) -> list[LostItemRecord]:
        return self.repository.get_all()

    def claim_bounty(self, item_id: str, claim: BountyClaim) -> LostItemRecord:
        item = self.repository.get_by_id(item_id)
        if item is None:
            raise ValueError(f"Lost item not found: {item_id}")

        if item.status is LostItemStatus.CLAIMED:
            raise ValueError(f"Lost item already claimed: {item_id}")

        print(f"Claim received from {claim.claimant_name} with proof {claim.proof_hash}")
        self.blockchain.release_funds(item.id)
        updated_item = item.model_copy(update={"status": LostItemStatus.CLAIMED})
        self.repository.update(updated_item)
        return updated_item
