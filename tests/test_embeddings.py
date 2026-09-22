from src.ai_knowledge_assistant.embeddings.embedder import EmbeddingModel

def test_embedding_model_returns_vector():

    embedder = EmbeddingModel()
    text = "FastAPI is a Python framework for building APIs."
    embedding = embedder.embed(text)

    assert isinstance(embedding, list)
    assert embedding != []
    assert all(isinstance(item, float) for item in embedding)
        
def test_embedding_model_returns_consistent_dimensions():

    embedder = EmbeddingModel()
    text_a = "FastAPI is a Python framework."
    text_b = "Vector databases store embeddings."
    embedding1 = embedder.embed(text_a)
    embedding2 = embedder.embed(text_b)

    assert len(embedding1) == len(embedding2)

def test_embedding_model_embeds_chunks():
    embedder = EmbeddingModel()

    chunks = [
        "FastAPI is a Python framework for building APIs.",
        "Vector databases store embeddings.",
        "LLMs generate responses from text."
    ]

    embeddings = embedder.embed_chunks(chunks)

    assert len(embeddings) == len(chunks)
    assert all(isinstance(embedding, list) for embedding in embeddings)
    assert all(
        isinstance(value, float)
        for embedding in embeddings
        for value in embedding
    )