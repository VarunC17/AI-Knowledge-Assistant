from fastapi import FastAPI
from src.ai_knowledge_assistant.application.service import(KnowledgeAssistantService)
from src.ai_knowledge_assistant.api.schemas import(
    AskRequest,
    AskResponse,
    )

app = FastAPI(title = "AI Knowledge Assistant")

service = KnowledgeAssistantService()

@app.get("/health")
def health_check():
    return service.health_check()

@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    answer = service.ask(request.question)

    return AskResponse(answer = answer)
