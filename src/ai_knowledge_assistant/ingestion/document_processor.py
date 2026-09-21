from pathlib import Path
from .text_loader import load_text_file
from .chunker import chunk_text

def load_and_chunk_text(path: Path)->list[str]:
    text = load_text_file(path)
    chunks = chunk_text(text)

    return chunks