from fastapi import FastAPI
from pydantic import BaseModel
from app.model import estimate_difficulty

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class DifficultyResponse(BaseModel):
    difficulty: int

@app.post("/predict", response_model=DifficultyResponse)
def predict_difficulty(req: TextRequest):
    score = estimate_difficulty(req.text)
    return {"difficulty": score}