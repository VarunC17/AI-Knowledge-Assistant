class KnowledgeAssistantService:
    def health_check(self)-> dict[str,str]:
        return {"status":"healthy"}
    def ask(self,question: str)->str:
        return f"Your question was received: {question}"
    