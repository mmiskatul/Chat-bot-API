from pydantic import BaseModel, Field

class ChatResponse(BaseModel):
    thinks: str = Field("", description="The model's thought process")
    ans: str = Field("", description="The final answer from the model")
