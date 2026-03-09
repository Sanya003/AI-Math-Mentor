import json
import os
from datetime import datetime

MEMORY_FILE = "memory/memory_log.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(
    original_input,
    parsed_problem,
    retrieved_context,
    final_answer,
    verifier_result
):

    memory = load_memory()

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": original_input,
        "parsed_problem": parsed_problem,
        "retrieved_context": retrieved_context,
        "final_answer": final_answer,
        "verifier_result": verifier_result
    }

    memory.append(entry)

    os.makedirs("memory", exist_ok=True)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def find_similar_memory(question):

    memory = load_memory()

    results = []

    for item in memory:
        if question.lower() in item["input"].lower():
            results.append(item)

    return results[:3]