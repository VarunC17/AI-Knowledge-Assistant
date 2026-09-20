from pathlib import Path

from src.ai_knowledge_assistant.ingestion.text_loader import load_text_file


def test_load_text_file():
    path = Path("data/sample.txt")

    content = load_text_file(path)

    assert "Retrieval-Augmented Generation" in content