from fastapi.testclient import TestClient

from src.ai_knowledge_assistant.api.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_ask():
    response = client.post(
        "/ask",
        json={"question": "What is RAG?"},
    )

    assert response.status_code == 200
    assert response.json() == {
        "answer": "Your question was received: What is RAG?"
    }


def test_ask_requires_question():
    response = client.post(
        "/ask",
        json={},
    )

    assert response.status_code == 422