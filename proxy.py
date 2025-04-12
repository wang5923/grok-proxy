# proxy.py
from fastapi import FastAPI, Request
from litellm import completion
import os

app = FastAPI()

# 设置为 xAI / Grok API 提供商
os.environ["LITELLM_PROVIDER"] = "xai"
os.environ["XAI_API_KEY"] = os.environ.get("XAI_API_KEY")  # 从环境变量读取密钥
os.environ["MODEL"] = "grok-8b"  # 根据需求更换模型名，如 grok-4b

@app.post("/v1/completions")
async def proxy_handler(request: Request):
    body = await request.json()
    response = completion(model=os.environ["MODEL"], messages=body["messages"])
    return response
