from fastapi.testclient import TestClient # Use the command to start unit tests: pytest -q --maxfail=2 --tb=line
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_read_hits():
    response = client.get("/hits")
    assert response.status_code == 200

def test_read_kfc(): 
    response = client.get("/kfc")
    assert response.status_code == 200
    assert response.headers.get('content-type') == 'application/json'
