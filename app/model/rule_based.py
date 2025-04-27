from .base import DifficultyEstimator
import fugashi

tagger = fugashi.Tagger()

class RuleBasedEstimator(DifficultyEstimator):
    def estimate(self, text: str) -> dict:
        words = [word.surface for word in tagger(text)]
        n = len(words)
        if n < 5:
            level = 1
        elif n < 10:
            level = 2
        elif n < 15:
            level = 3
        elif n < 20:
            level = 4
        else:
            level = 5

        return {
            "difficulty": level,
            "word_count": n,
            "method": "rule_based"
        }