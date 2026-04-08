from pydantic import BaseModel

class Observation(BaseModel):
    state: str

class Action(BaseModel):
    action: str

class AIWorkOpsEnv:
    def __init__(self):
        self.step_count = 0

    def reset(self):
        self.step_count = 0
        return Observation(state="Start")

    def step(self, action: Action):
        self.step_count += 1
        reward = 1.0 if "correct" in action.action else 0.5
        done = self.step_count >= 3
        return Observation(state="Next Step"), reward, done, {}

    def state(self):
        return {"step": self.step_count}
