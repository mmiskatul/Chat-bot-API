from fastapi import FastAPI
from schemas.chat_schema import ChatRequest, ChatResponse
from models.qwen_model import qwen_model

app = FastAPI(
    title="Qwen Text Generation API",
    description="FastAPI + HuggingFace Qwen Model",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    response_text = qwen_model.generate(
        prompt=request.prompt,
        max_new_tokens=request.max_new_tokens,
        temperature=request.temperature
    )
    return ChatResponse(response=response_text)
