import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1:8b"


def explain_solution(solution):

    prompt = f"""
        Explain this math solution in a simple way for a JEE student.

        SOLUTION:
        {solution}
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return solution

    return response.json()["response"]