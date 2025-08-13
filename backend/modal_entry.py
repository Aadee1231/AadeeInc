from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import modal

app = modal.App("aadee-multiagent-backend")

image = modal.Image.debian_slim().pip_install("fastapi[standard]")

fastapi_app = FastAPI()

fastapi_app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.function(image=image)
@modal.concurrent(max_inputs=100)
@modal.asgi_app()

def serve():
    return fastapi_app