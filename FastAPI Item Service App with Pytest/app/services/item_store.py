from datetime import datetime, timezone
from uuid import uuid4

from app.schemas.item import ItemCreate, ItemRead, ItemUpdate


class ItemNotFoundError(LookupError):
    pass


class ItemStore:
    def __init__(self) -> None:
        self._items: dict[str, ItemRead] = {}

    def seed_demo_items(self) -> None:
        if self._items:
            return

        self.create_item(
            ItemCreate(
                name="FastAPI starter kit",
                description="Seed item used for demonstrations and smoke tests.",
                price=49.99,
                tags=["seed", "demo"],
            )
        )
        self.create_item(
            ItemCreate(
                name="API observability pack",
                description="A sample inactive item for filtering checks.",
                price=19.5,
                tags=["observability", "sample"],
                is_active=False,
            )
        )

    def list_items(self, include_inactive: bool = False) -> list[ItemRead]:
        items = sorted(self._items.values(), key=lambda item: item.created_at, reverse=True)
        if include_inactive:
            return items
        return [item for item in items if item.is_active]

    def create_item(self, payload: ItemCreate) -> ItemRead:
        now = datetime.now(timezone.utc)
        item = ItemRead(
            id=str(uuid4()),
            created_at=now,
            updated_at=now,
            **payload.model_dump(),
        )
        self._items[item.id] = item
        return item

    def get_item(self, item_id: str) -> ItemRead:
        try:
            return self._items[item_id]
        except KeyError as exc:
            raise ItemNotFoundError(item_id) from exc

    def update_item(self, item_id: str, payload: ItemUpdate) -> ItemRead:
        current_item = self.get_item(item_id)
        updates = payload.model_dump(exclude_unset=True)

        if not updates:
            return current_item

        updated_item = current_item.model_copy(
            update=updates | {"updated_at": datetime.now(timezone.utc)}
        )
        self._items[item_id] = updated_item
        return updated_item

    def delete_item(self, item_id: str) -> ItemRead:
        item = self.get_item(item_id)
        self._items.pop(item_id)
        return item