from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {"status": "ok"}

# Health check
@app.get("/health")
def health():
    return {"status": "healthy"}

# REQUIRED for OpenEnv
@app.post("/reset")
def reset():
    return {"observation": "environment reset"}

# REQUIRED for OpenEnv
@app.post("/step")
def step(action: dict):
    return {
        "observation": "next state",
        "reward": 1,
        "done": False,
        "info": {}
    }

# Optional
@app.post("/predict")
def predict(data: dict):
    return {"prediction": "dummy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
