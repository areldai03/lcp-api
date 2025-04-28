from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_api():
    response = client.post("/predict", json={"text": "これはAPIテストの文章ですにゃ。"})
    assert response.status_code == 200

    data = response.json()

    # レスポンスにdifficultyが含まれること
    assert "difficulty" in data
    # difficultyは1〜5の範囲であること
    assert 1 <= data["difficulty"] <= 5

    # method情報が含まれること
    assert "method" in data
