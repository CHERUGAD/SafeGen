from fastapi import FastAPI
from pydantic import BaseModel
from app.prompt_guard import PromptGuard

app = FastAPI()
guard = PromptGuard()

class PromptInput(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "SafeGen is running!"}

@app.post("/check_prompt")
def check_prompt(data: PromptInput):
    status = guard.check_prompt(data.prompt)
    is_safe = status == "safe"
    return {
        "prompt": data.prompt,
        "is_safe": is_safe,
        "status": "✅ SAFE" if is_safe else "❌ UNSAFE"
    }
