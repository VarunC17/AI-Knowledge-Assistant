from fastapi.testclient import TestClient

from src.ai_knowledge_assistant.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status":"healthy"}