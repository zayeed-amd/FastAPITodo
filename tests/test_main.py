from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def register_and_login(username="testuser", password="secret"):
    # Register
    client.post("/auth/register", json={"username": username, "password": password})
    # Login
    resp = client.post("/auth/token", data={"username": username, "password": password})
    assert resp.status_code == 200
    token = resp.json()["access_token"]
    return token

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "message" in r.json()

def test_todo_crud_flow():
    token = register_and_login()
    headers = {"Authorization": f"Bearer {token}"}

    # Create
    r = client.post("/todos", json={"title": "Buy milk", "completed": False}, headers=headers)
    assert r.status_code == 201
    todo = r.json()
    todo_id = todo["id"]

    # Read list
    r = client.get("/todos", headers=headers)
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert any(t["id"] == todo_id for t in r.json())

    # Update
    r = client.put(f"/todos/{todo_id}", json={"completed": True}, headers=headers)
    assert r.status_code == 200
    assert r.json()["completed"] is True

    # Get single
    r = client.get(f"/todos/{todo_id}", headers=headers)
    assert r.status_code == 200
    assert r.json()["id"] == todo_id

    # Delete
    r = client.delete(f"/todos/{todo_id}", headers=headers)
    assert r.status_code == 204
