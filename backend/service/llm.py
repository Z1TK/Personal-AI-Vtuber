import os


class LLMClient:
    def __init__(self, model: str, host: str) -> None:
        self.model = model
        self.host = host
        self.api_key = os.environ.get("OLLAMA_API_KEY")

    def ask(self, prompt: str) -> dict:
        url = f"{self.host}/api/generate"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {"model": self.model, "prompt": prompt}

        return {"url": url, "headers": headers, "data": data}

    def conversation(self, content: str, charater: str) -> dict:
        pass
