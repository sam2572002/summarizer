from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_summarize():
    
    response = client.post("/summarize", json={"text": "Hello there!"})
    assert response.status_code == 200
    assert "summary" in response.json()    

def test_bullets():
    
    response = client.post("/summarize/bullets", json={"text": "Hello there!"})
    assert response.status_code == 200
    assert "bullets" in response.json()     

def test_sentiment():    
    response = client.post("/summarize/sentiment", json={"text": "Hello there!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
    assert "reason" in response.json()

def test_history():    
    response = client.get("/history")
    assert response.status_code == 200
    assert isinstance(response.json(), list)         

def test_delete(): 
    client.post("/summarize",json={"text": "some text"})
    id = client.get("/history").json()[-1]["id"]
    response = client.delete(f"/history/{id}")
    assert response.status_code == 200
    assert "message" in response.json()