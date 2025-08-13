import modal

app = modal.App("aadee-multiagent-backend")
image = modal.Image.debian_slim().pip_install("fastapi[standard]")

@app.function(image=image)
@modal.asgi_app()
def serve():
    from main import app as fastapi_app
    return fastapi_app
