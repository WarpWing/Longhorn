from fastapi.testclient import TestClient # Use the command to start unit tests: pytest --maxfail=2 --tb=line
from main import app
import requests 

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200 # Does a Status Code Check 

def test_read_hits():
    response = client.get("/hits")
    assert response.status_code == 200 # Does a Status Code Check 
    assert response.headers.get('content-type') == 'application/json' # Does a check on content type to ensure the response is JSON

def test_read_kfc(): 
    response = client.get("/kfc")
    assert response.status_code == 200 # Does a Status Code Check 
    assert response.headers.get('content-type') == 'application/json' # Does a check on content type to ensure the response is JSON

print("This is a Python Unit Test. Use the command to start unit tests: pytest --maxfail=2 --tb=line") # Outputs this if executed as a normal python file 

