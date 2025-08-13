import modal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

web = FastAPI()
web.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@web.get("/ping")
def ping():
    return {"message": "pong from multi-agent backend"}

app = modal.App("aadee-multiagent-backend")
image = modal.Image.debian_slim().pip_install("fastapi[standard]")

@app.function(image=image)
@modal.asgi_app()
def serve():
    return web
