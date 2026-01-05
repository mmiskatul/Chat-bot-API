from transformers import pipeline
from config.settings import settings
import re

class QwenModel:
    def __init__(self):
        print("Loading Qwen model...")
        self.pipe = pipeline(
            "text-generation",
            model=settings.model_name,
            device=settings.device
        )
        print("Model loaded!")

    def generate(self, prompt: str, max_new_tokens: int = None, temperature: float = None) -> dict:
        max_new_tokens = max_new_tokens or settings.max_new_tokens
        temperature = temperature or settings.temperature

        messages = [{"role": "user", "content": prompt}]
        output = self.pipe(
            messages,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature
        )

        text = output[0]["generated_text"][-1]["content"]

        # Extract <think> section
        thinks_match = re.search(r"<think>(.*?)</think>", text, flags=re.DOTALL)
        thinks = thinks_match.group(1).strip() if thinks_match else ""

        # Remove <think> section for final answer
        ans = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

        return {"thinks": thinks, "ans": ans}

qwen_model = QwenModel()
