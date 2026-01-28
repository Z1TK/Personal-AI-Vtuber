import requests

from backend.service.llm import LLMClient


def ask_assistent(llm_engine: LLMClient, prompt: str) -> dict:
    request = llm_engine.ask(prompt=prompt)
    r = requests.post(
        url=request["url"], headers=request["headers"], json=request["data"]
    )

    try:
        return r.json()
    except:
        print("Ошибка JSON:", r.text)
        return {"error": r.text}
