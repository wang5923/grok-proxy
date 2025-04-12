# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY proxy.py .

CMD ["uvicorn", "proxy:app", "--host", "0.0.0.0", "--port", "4000"]
