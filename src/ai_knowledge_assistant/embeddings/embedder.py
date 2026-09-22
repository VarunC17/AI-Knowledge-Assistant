from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


class EmbeddingModel:
    def __init__(self) -> None:
        self.model = SentenceTransformer(MODEL_NAME)

    def embed(self, text: str) -> list[float]:
        embedding = self.model.encode(text)
        return embedding.tolist()

    def embed_chunks(self, chunks: list[str])-> list[list[float]]:
        embedding = self.model.encode(chunks)
        return [embeddings.tolist() for embeddings in embedding]
    
    