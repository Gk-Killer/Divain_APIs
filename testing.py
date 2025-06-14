from fastapi.testclient import TestClient
from Divain.main import app

client = TestClient(app)

def test_get_stocks_success():
    response = client.get("/stocks")
    assert response.status_code == 200 or response.status_code == 404  # Adjust based on your test DB state
    assert "stocks" in response.json() or "detail" in response.json()

def test_update_stock_movement_success():
    response = client.post("/stocks_movement", json={
        "stock_id": "ITEM001",
        "mov_quantity": 5,
        "mov_type": "in"
    })
    assert response.status_code == 200
    assert response.json() == {"message": "Stock movement updated successfully"}

def test_history_stock_mov():
    response = client.post("/stocks_movement_history")
    assert response.status_code == 200 or response.status_code == 404
    assert "stocks History" in response.json() or "detail" in response.json()