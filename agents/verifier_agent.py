import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1:8b"


def verify_solution(question, solution):

    prompt = f"""
        You are a mathematics verifier.

        Check if the following solution is correct.

        QUESTION:
        {question}

        SOLUTION:
        {solution}

        Return:
        1. Whether the solution is correct
        2. A confidence score between 0 and 1
        3. A short explanation
    """

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return 0.0, "Verification failed"

    text = response.json()["response"]

    return 0.8, text