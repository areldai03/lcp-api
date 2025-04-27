from fastapi import FastAPI, Query
from pydantic import BaseModel
from app.model import RuleBasedEstimator, WordfreqBasedEstimator, EmbeddingBasedEstimator

app = FastAPI()

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