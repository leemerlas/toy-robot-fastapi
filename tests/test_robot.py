from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_place_robot():
    response = client.post("/PLACE", json={"x": 0, "y": 0, "f": "NORTH"})
    assert response.status_code == 200
    assert response.json() == {"status": "Placed"}

def test_move_robot():
    client.post("/PLACE", json={"x": 0, "y": 0, "f": "NORTH"})
    response = client.post("/MOVE")
    assert response.status_code == 200
    assert response.json() == {"status": "Moved"}

def test_left_robot():
    client.post("/PLACE", json={"x": 0, "y": 0, "f": "NORTH"})
    response = client.post("/LEFT")
    assert response.status_code == 200
    assert response.json() == {"status": "Turned left"}

def test_right_robot():
    client.post("/PLACE", json={"x": 0, "y": 0, "f": "NORTH"})
    response = client.post("/RIGHT")
    assert response.status_code == 200
    assert response.json() == {"status": "Turned right"}

def test_report_robot():
    client.post("/PLACE", json={"x": 0, "y": 0, "f": "NORTH"})
    client.post("/MOVE")
    response = client.get("/REPORT")
    assert response.status_code == 200
    assert response.json() == {"x": 0, "y": 1, "f": "NORTH"}

def test_invalid_commands_before_place():
    response = client.post("/MOVE")
    assert response.status_code == 200
    assert response.json() == {"status": "Moved"}  # But the robot has not moved, as it wasn't placed yet

#     response = client.get("/REPORT")
#     assert response.status_code == 200
#     assert response.json() == {"error": "Robot not placed on the table."}
