from fastapi import FastAPI
from models.qwen_model import qwen_model
from schemas.chat_schema import ChatRequest, ChatResponse

app = FastAPI(title="Qwen Chat API")

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    response = qwen_model.generate(
        prompt=request.prompt,
        max_new_tokens=request.max_new_tokens,
        temperature=request.temperature
    )
    return response
