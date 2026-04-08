from fastapi import FastAPI
from app import app as env_app  # import your actual env

app = env_app

# Add health route (important)
@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}
