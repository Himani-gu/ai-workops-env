from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: dict):
    # Replace with your actual model logic
    return {"prediction": "your_output"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
