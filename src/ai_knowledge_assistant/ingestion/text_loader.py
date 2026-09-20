from pathlib import Path


def load_text_file(path: Path) -> str:
    with path.open("r", encoding="utf-8") as file:
        return file.read()