from __future__ import annotations

from myapp.core.domain import LostItemRecord


class BountyRepository:
    def __init__(self) -> None:
        self._items: dict[str, LostItemRecord] = {}

    def add(self, item: LostItemRecord) -> LostItemRecord:
        self._items[item.id] = item
        return item

    def get_all(self) -> list[LostItemRecord]:
        return list(self._items.values())

    def get_by_id(self, item_id: str) -> LostItemRecord | None:
        return self._items.get(item_id)

    def update(self, item: LostItemRecord) -> LostItemRecord:
        if item.id not in self._items:
            raise ValueError(f"Lost item not found: {item.id}")
        self._items[item.id] = item
        return item
