import fugashi
from wordfreq import word_frequency

tagger = fugashi.Tagger()

def estimate_difficulty_with_wordfreq(text: str) -> dict:
    """
    入力文の難易度を wordfreq を使って推定
    """
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
        "total_words": total,
        "difficult_words": difficult_words,
        "average_frequency": avg_freq,
    }

def estimate_difficulty(text: str) -> int:
    """
    入力文の難易度をルールベースで推定 (とりあえず簡易版)
    - 文字数や単語数などをベースにした難易度スコア
    """
    if not text.strip():
        return 1

    words = text.split()
    length = len(words)

    if length < 5:
        return 1
    elif length < 10:
        return 2
    elif length < 15:
        return 3
    elif length < 20:
        return 4
    else:
        return 5
