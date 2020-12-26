from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200 

def test_read_hits():
    response = client.get("/hits")
    assert response.status_code == 200
