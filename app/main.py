from fastapi import FastAPI
from pydantic import BaseModel
from app.model import estimate_difficulty, estimate_difficulty_with_wordfreq

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class DifficultyResponse(BaseModel):
    difficulty: int

@app.post("/predict-length", response_model=DifficultyResponse)
def predict_length_difficulty(req: TextRequest):
    score = estimate_difficulty(req.text)
    return {"difficulty": score}

@app.post("/predict-freq", response_model=dict)
def predict_freq_difficulty(req: TextRequest):
    result = estimate_difficulty_with_wordfreq(req.text)
    return result