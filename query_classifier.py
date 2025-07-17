class QueryClassifier:
    def classify(self, query: str) -> str:
        context = query.lower()
        
        if any(kw in context for kw in ["define", "meaning", "what is", "who is"]):
            return "definition"
        elif any(kw in context for kw in ["how", "steps", "procedure", "guide"]):
            return "process"
        elif any(kw in context for kw in ["why", "importance", "reason"]):
            return "reasoning"
        elif any(kw in context for kw in ["remember", "previous", "before", "earlier"]):
            return "contextual"
        else:
            return "general"