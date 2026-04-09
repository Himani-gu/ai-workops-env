from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr
import threading

app = FastAPI()

# -----------------------
# API endpoints
# -----------------------
@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}

class Action(BaseModel):
    action: int

@app.post("/reset")
def reset():
    return {"observation": "environment reset", "reward": 0, "done": False, "info": {}}

@app.post("/step")
def step(action: Action):
    return {"observation": f"next state after action {action.action}", "reward": 1, "done": False, "info": {}}

# -----------------------
# Gradio frontend
# -----------------------
def reset_ui():
    return "Environment reset!"

def step_ui(action):
    return f"Next state after action {action}"

with gr.Blocks() as demo:
    gr.Markdown("## AI WorkOps Env Testing UI")
    with gr.Row():
        reset_btn = gr.Button("Reset Environment")
        reset_output = gr.Textbox(label="Reset Output")
        step_input = gr.Number(label="Action (integer)")
        step_btn = gr.Button("Perform Step")
        step_output = gr.Textbox(label="Step Output")
    
    reset_btn.click(reset_ui, [], reset_output)
    step_btn.click(step_ui, [step_input], step_output)

def run_gradio():
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)

# Run Gradio in a separate thread so FastAPI still works
threading.Thread(target=run_gradio, daemon=True).start()
