class ContextManager:
    def __init__(self):
        self.conversation_history = []
        self.entities = {}
    
    def add_to_history(self, role: str, content: str):
        self.conversation_history.append({"role": role, "content": content})
        self.update_entities(content)
    
    def update_entities(self, text: str):
         # Basic entity extraction based on simple keyword matching
        if "my name is" in text.lower():
            name = text.split("my name is")[-1].split()[0].strip()
            self.entities["user_name"] = name
        elif "I live in" in text.lower():
            location = text.split("I live in")[-1].split()[0].strip()
            self.entities["user_location"] = location
    
    def get_context_prompt(self):
        
        context = ""
        
        if self.entities:
            context += "Known Context:\n"
            for key, value in self.entities.items():
                context += f"- {key.replace('_', ' ').title()}: {value}\n"
            context += "\n"
        
        
        if self.conversation_history:
            context += "Conversation History:\n"
            for msg in self.conversation_history[-4:]:  # Last 4 messages
                prefix = "User" if msg["role"] == "user" else "Assistant"
                context += f"{prefix}: {msg['content']}\n"
        
        return context.strip()
        
    def __str__(self):
    return f"ContextManager(Entities: {self.entities}, History Count: {len(self.conversation_history)})"

    def clear_history(self):
        self.conversation_history = []
        self.entities = {}
