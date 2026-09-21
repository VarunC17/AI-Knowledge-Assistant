import re


def chunk_text(text: str) -> list[str]:
    paragraphs = re.split(r"\n\s*\n", text)

    chunks = []

    for paragraph in paragraphs:
        paragraph = paragraph.strip()

        if paragraph:
            chunks.append(paragraph)

    return chunks