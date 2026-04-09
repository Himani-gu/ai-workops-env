from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {"status": "ok"}

# Health endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Input model for step
class Action(BaseModel):
    action: int

# Reset endpoint
@app.post("/reset")
def reset():
    return {
        "observation": "environment reset",
        "reward": 0,
        "done": False,
        "info": {}
    }

# Step endpoint
@app.post("/step")
def step(action: Action):
    return {
        "observation": f"next state after action {action.action}",
        "reward": 1,
        "done": False,
        "info": {}
    }
