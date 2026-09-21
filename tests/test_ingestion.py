from pathlib import Path

import re

from src.ai_knowledge_assistant.ingestion.text_loader import load_text_file

from src.ai_knowledge_assistant.ingestion.chunker import chunk_text

from src.ai_knowledge_assistant.ingestion.document_processor import load_and_chunk_text


def test_load_text_file():
    path = Path("data/sample.txt")

    content = load_text_file(path)

    assert "Retrieval-Augmented Generation" in content

def test_chunk_text_multiple_paragraphs():
    
    text = "Python is a Programming Language \n\n FastAPI is a python framework for building APIs \n\n Vector databases store embeddings"

    chunks = chunk_text(text)

    expected_chunks = [
        "Python is a Programming Language",
        "FastAPI is a python framework for building APIs",
        "Vector databases store embeddings"
    ]

    assert chunks == expected_chunks

def test_chunk_text_ignores_empty_paragraphs():

    text = "First Paragraph\n\n\n\nSecond Paragraph\n\n\n\nThird Paragraph"

    chunks = chunk_text(text)

    expected_chunk = [
        "First Paragraph",
        "Second Paragraph",
        "Third Paragraph"
    ]

    assert chunks == expected_chunk

def test_chunk_text_strips_chunk_whitespace():

    text = "   First paragraph.   \n\n   Second paragraph.   "

    chunks = chunk_text(text)

    expected_chunk = [
        "First paragraph.",
        "Second paragraph."
    ]

    assert chunks == expected_chunk

def test_chunk_text_with_empty_text():

    text = ""

    chunks = chunk_text(text)
    assert chunks == []

def test_load_and_chunk_text():
    path = Path("data/sample.txt")

    chunks = load_and_chunk_text(path)

    assert isinstance(chunks, list)
    assert all(isinstance(chunk, str) for chunk in chunks)

    expected_text = path.read_text(encoding="utf-8")

    expected_paragraphs = re.split(r"\n\s*\n", expected_text) 

    expected_chunks = [paragraph.strip() for paragraph in expected_paragraphs if paragraph.strip()]

    assert chunks == expected_chunks