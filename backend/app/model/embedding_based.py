from .base import DifficultyEstimator
from transformers import pipeline
import numpy as np

model_name = "line-corporation/line-distilbert-base-japanese"

feature_extractor = pipeline("feature-extraction", model=model_name, tokenizer=model_name, device=-1, trust_remote_code=True)

class EmbeddingBasedEstimator(DifficultyEstimator):
    def estimate(self, text: str) -> dict:
        embeddings_list = feature_extractor(text)
        embeddings = np.array(embeddings_list[0]).mean(axis=0)

        norm = np.linalg.norm(embeddings)
        variance = np.var(embeddings)
        # 線形層を本当は置きたい😢
        if norm < 25:
            level = 1
        elif norm < 50:
            level = 2
        elif norm < 75:
            level = 3
        elif norm < 100:
            level = 4
        else:
            level = 5

        return {
            "difficulty": level,
            "embedding_norm": float(norm),
            "embedding_variance": float(variance),
            "method": "embedding"
        }