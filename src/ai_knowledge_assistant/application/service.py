class KnowledgeAssistantService:
    def health_check(self)-> dict[str,str]:
        return {"status":"healthy"}