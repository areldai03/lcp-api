from .base import DifficultyEstimator
from wordfreq import word_frequency
import fugashi

tagger = fugashi.Tagger()

class WordfreqBasedEstimator(DifficultyEstimator):
    def estimate(self, text: str) -> dict:
        words = [word.surface for word in tagger(text)]
        total = len(words)
        difficult_words = []
        freq_scores = []

        for w in words:
            freq = word_frequency(w, "ja", wordlist='best')
            freq_scores.append(freq)
            if freq < 1e-5:
                difficult_words.append(w)

        avg_freq = sum(freq_scores) / total if total else 0

        if avg_freq > 0.01:
            level = 1
        elif avg_freq > 0.005:
            level = 2
        elif avg_freq > 0.001:
            level = 3
        elif avg_freq > 0.0001:
            level = 4
        else:
            level = 5

        return {
            "difficulty": level,
            "word_count": total,
            "difficult_words": difficult_words,
            "average_frequency": avg_freq,
            "method": "wordfreq"
        }
