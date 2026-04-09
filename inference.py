# inference.py

from fastapi import FastAPI, Request
import uvicorn
import json

app = FastAPI()

# Health check endpoint
@app.get("/ping")
def ping():
    return {"status": "ok"}

# Inference endpoint
@app.post("/predict")
async def predict(request: Request):
    """
    Expects JSON input.
    Replace the dummy logic below with your model inference.
    """
    try:
        data = await request.json()
        # Dummy response; replace with your model's actual prediction
        prediction = {"prediction": "dummy_result", "input_received": data}
        return prediction
    except Exception as e:
        return {"error": str(e)}

# Allow running locally for testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
