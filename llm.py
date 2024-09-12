from langchain_ollama import OllamaLLM

def initialize_llm():
   
    return OllamaLLM(model="mistral:7b")
