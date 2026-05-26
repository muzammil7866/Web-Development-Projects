def test_list_items_returns_seed_data(client):
    response = client.get("/items")

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["name"] == "FastAPI starter kit"


def test_item_crud_flow(client):
    payload = {
        "name": "Project blueprint",
        "description": "Structured item used to verify CRUD behavior.",
        "price": 99.0,
        "tags": ["crud", "api"],
    }

    create_response = client.post("/items", json=payload)
    assert create_response.status_code == 201

    created_item = create_response.json()
    item_id = created_item["id"]

    fetch_response = client.get(f"/items/{item_id}")
    assert fetch_response.status_code == 200
    assert fetch_response.json()["name"] == payload["name"]

    update_response = client.patch(
        f"/items/{item_id}",
        json={"price": 120.5, "is_active": False},
    )
    assert update_response.status_code == 200
    assert update_response.json()["price"] == 120.5
    assert update_response.json()["is_active"] is False

    delete_response = client.delete(f"/items/{item_id}")
    assert delete_response.status_code == 200

    missing_response = client.get(f"/items/{item_id}")
    assert missing_response.status_code == 404