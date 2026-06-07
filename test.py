from fastapi.testclient import TestClient
from main import app
import time


client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_summarize():
    time.sleep(5)
    response = client.post("/summarize", json={"text": "Hello there!"})
    assert response.status_code == 200
    assert "summary" in response.json()    

def test_bullets():
    time.sleep(5)
    response = client.post("/summarize/bullets", json={"text": "Hello there!"})
    assert response.status_code == 200
    assert "bullets" in response.json()     

def test_sentiment():    
    time.sleep(5)
    response = client.post("/summarize/sentiment", json={"text": "Hello there!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
    assert "reason" in response.json()

def test_history():    
    response = client.get("/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)         

def test_delete(): 
    id = client.get("/history").json()[-1]["id"]
    response = client.delete(f"/history/{id}")
    assert response.status_code == 200
    assert "message" in response.json()