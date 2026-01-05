from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(..., description="The user input prompt")
    max_new_tokens: int = Field(200, ge=1, le=1000, description="Maximum number of tokens to generate")
    temperature: float = Field(0.7, ge=0.0, le=1.0, description="Sampling temperature for text generation")

class ChatResponse(BaseModel):
    thinks: str = Field("", description="The model's thought process")
    ans: str = Field("", description="The final answer from the model")
