import torch
from transformers import pipeline
from config.settings import settings

class QwenModel:
    def __init__(self):
        print("Loading Qwen model... this may take a while")
        self.pipe = pipeline(
            "text-generation",
            model=settings.model_name,
            device=settings.device
        )
        print("Model loaded successfully!")

    def generate(self, prompt: str, max_new_tokens: int, temperature: float) -> str:
        messages = [{"role": "user", "content": prompt}]
        output = self.pipe(
            messages,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature
        )
        return output[0]["generated_text"][-1]["content"]

# Initialize model once
qwen_model = QwenModel()
