from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {"status": "ok"}

# Health endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# OpenEnv reset endpoint
@app.post("/reset")
def reset():
    return {
        "observation": "environment reset",
        "reward": 0,
        "done": False,
        "info": {}
    }

# OpenEnv step endpoint
@app.post("/step")
def step(action: dict):
    return {
        "observation": "next state",
        "reward": 1,
        "done": False,
        "info": {}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
