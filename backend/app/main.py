from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.model import RuleBasedEstimator, WordfreqBasedEstimator, EmbeddingBasedEstimator
from .config import Config

app = FastAPI()

config = Config()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_difficulty(req: TextRequest, method: str = Query("wordfreq")):
    if method == "rule":
        estimator = RuleBasedEstimator()
    elif method == "wordfreq":
        estimator = WordfreqBasedEstimator()
    elif method == "embedding":
        estimator = EmbeddingBasedEstimator()
    
    result = estimator.estimate(req.text)
    return result