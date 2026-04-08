from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Models
class Action(BaseModel):
    action: str

# Environment state
state = {"step": 0}

# RESET endpoint
@app.post("/reset")
def reset():
    state["step"] = 0
    return {"observation": "Start"}

# STEP endpoint
@app.post("/step")
def step(action: Action):
    state["step"] += 1

    reward = 1.0 if "correct" in action.action else 0.5
    done = state["step"] >= 3

    return {
        "observation": "Next Step",
        "reward": reward,
        "done": done,
        "info": {}
    }

# STATE endpoint
@app.get("/state")
def get_state():
    return state
