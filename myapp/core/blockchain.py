from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from secrets import token_hex

@dataclass
class SimulatedBlockchain:
    transactions: list[dict[str, str]] = field(default_factory=list)


    def create_escrow(self, amount: str, owner_oib: str) -> str:
        tx_hash = token_hex(16)
        message = f"Creating escrow for owner {owner_oib} and amount {amount}"
        print(message)
        self.transactions.append(
            {
                "type": "create_escrow",
                "amount": str(amount),
                "owner_oib": owner_oib,
                "tx_hash": tx_hash,
                "timestamp": datetime.utcnow().isoformat(),
                "message": message,
            }
        )
        return tx_hash

    def release_funds(self, bounty_id: str) -> None:
        message = f"Releasing funds for bounty {bounty_id}"
        print(message)
        self.transactions.append(
            {
                "type": "release_funds",
                "bounty_id": bounty_id,
                "timestamp": datetime.utcnow().isoformat(),
                "message": message,
            }
        )
