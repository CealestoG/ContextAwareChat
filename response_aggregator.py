from autogen import AssistantAgent
from typing import List

class ResponseAggregator:
    def __init__(self):
        self.agent = AssistantAgent(name="ResponseAggregator")

    def aggregate(self, responses: List[str]) -> str:
        if not responses:
            return "No responses to aggregate."

        if len(responses) == 1:
            return responses[0]

        combined = "\n\n".join(responses)
        return combined
