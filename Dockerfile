FROM python:3.10-slim

RUN apt update && apt install -y mecab libmecab-dev mecab-ipadic-utf8 && \
    pip install fastapi uvicorn fugashi

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]