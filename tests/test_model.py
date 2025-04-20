import pytest
from app.model import estimate_difficulty

@pytest.mark.parametrize("text,expected", [
    ("", 1),
    ("i have an apple.", 1),
    ("i don't have an apple.", 2),
    ("i "*14, 3),
    ("i "*19, 4),
    ("i "*20, 5),
])
def test_estimate_difficulty(text, expected):
    assert estimate_difficulty(text) == expected
