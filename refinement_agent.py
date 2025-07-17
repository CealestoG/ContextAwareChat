from autogen import AssistantAgent

class RefinementAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="RefinementAgent")

    def refine(self, aggregated_response: str) -> str:
        if not aggregated_response:
            return "Nothing to refine."

        return aggregated_response.strip()
