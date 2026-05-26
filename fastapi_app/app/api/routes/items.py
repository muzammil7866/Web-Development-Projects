from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import get_item_store
from app.schemas.item import ItemCreate, ItemRead, ItemUpdate
from app.services.item_store import ItemNotFoundError, ItemStore


router = APIRouter(prefix="/items", tags=["Items"])


def _not_found(item_id: str) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item '{item_id}' was not found")


@router.get("", response_model=list[ItemRead])
def list_items(
    include_inactive: bool = False,
    item_store: ItemStore = Depends(get_item_store),
) -> list[ItemRead]:
    return item_store.list_items(include_inactive=include_inactive)


@router.post("", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(
    payload: ItemCreate,
    item_store: ItemStore = Depends(get_item_store),
) -> ItemRead:
    return item_store.create_item(payload)


@router.get("/{item_id}", response_model=ItemRead)
def get_item(item_id: str, item_store: ItemStore = Depends(get_item_store)) -> ItemRead:
    try:
        return item_store.get_item(item_id)
    except ItemNotFoundError as exc:
        raise _not_found(item_id) from exc


@router.patch("/{item_id}", response_model=ItemRead)
def update_item(
    item_id: str,
    payload: ItemUpdate,
    item_store: ItemStore = Depends(get_item_store),
) -> ItemRead:
    try:
        return item_store.update_item(item_id, payload)
    except ItemNotFoundError as exc:
        raise _not_found(item_id) from exc


@router.delete("/{item_id}", response_model=ItemRead)
def delete_item(item_id: str, item_store: ItemStore = Depends(get_item_store)) -> ItemRead:
    try:
        return item_store.delete_item(item_id)
    except ItemNotFoundError as exc:
        raise _not_found(item_id) from exc