FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \ 
    pip install -r requirements.txt

COPY bot.py .
COPY commands/ ./commands/
COPY core/ ./core/

CMD ["python", "-u", "bot.py"]
