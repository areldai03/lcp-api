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
