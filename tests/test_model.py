import pytest

from app.model import RuleBasedEstimator, WordfreqBasedEstimator, EmbeddingBasedEstimator

test_cases = [
    (RuleBasedEstimator, "これは簡単な文章です。"),
    (WordfreqBasedEstimator, "これは簡単な文章です。"),
    (EmbeddingBasedEstimator, "これは簡単な文章です。"),
]

@pytest.mark.parametrize("EstimatorClass,text", test_cases)
def test_estimator(EstimatorClass, text):
    estimator = EstimatorClass()
    result = estimator.estimate(text)

    assert isinstance(result, dict)

    assert "difficulty" in result

    assert 1 <= result["difficulty"] <= 5