from fastapi import FastAPI, Query
from pydantic import BaseModel
from app.model.rule_based import RuleBasedEstimator
from app.model.wordfreq_based import WordfreqBasedEstimator

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_difficulty(req: TextRequest, method: str = Query("wordfreq")):
    if method == "rule":
        estimator = RuleBasedEstimator()
    else:
        estimator = WordfreqBasedEstimator()

    result = estimator.estimate(req.text)
    return result