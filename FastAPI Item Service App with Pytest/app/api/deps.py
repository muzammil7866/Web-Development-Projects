from fastapi import Request

from app.services.item_store import ItemStore


def get_item_store(request: Request) -> ItemStore:
    return request.app.state.item_store