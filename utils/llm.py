from langchain_community.llms import Ollama

def load_llm():
    llm = Ollama(
        model="llama3.1:8b",
        temperature=0.2
    )
    return llm