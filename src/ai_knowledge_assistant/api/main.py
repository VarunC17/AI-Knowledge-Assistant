from fastapi import FastAPI
from src.ai_knowledge_assistant.application.service import(KnowledgeAssistantService)

app = FastAPI(title = "AI Knowledge Assistant")

service = KnowledgeAssistantService()

@app.get("/health")
def health_check():
    return service.health_check()

