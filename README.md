# Grok Proxy (xAI API Forwarder)

A lightweight proxy server for forwarding requests to Elon Musk's xAI / Grok API using LiteLLM and FastAPI.

## 🔧 Features

- Supports `/v1/completions` endpoint
- Configurable model (e.g., `grok-8b`, `grok-4b`)
- Dockerized for deployment on small VPS (512MB RAM)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourname/grok-proxy.git
cd grok-proxy
### 2. Build the Docker image
docker build -t grok-proxy .
### 3. Run the container
docker run -d \
  --name grok-proxy \
  -e XAI_API_KEY="your_xai_api_key" \
  -p 4000:4000 \
  grok-proxy
### 📡 Example Request
curl http://localhost:4000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Tell me a joke about space"}]
  }'
