import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.1:8b"


def solve_problem(question, parsed_problem, context):

    prompt = f"""
You are an expert JEE mathematics tutor.

Solve the following problem step-by-step.

Use the provided context if helpful.

--------------------------------
QUESTION:
{question}

--------------------------------
PARSED STRUCTURE:
{parsed_problem}

--------------------------------
KNOWLEDGE CONTEXT:
{context}

--------------------------------
INSTRUCTIONS:
- Show clear mathematical steps
- Explain reasoning
- Provide the final answer clearly
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        return "Solver model failed."

    result = response.json()

    return result["response"]