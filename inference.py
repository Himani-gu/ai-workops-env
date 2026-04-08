from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/reset")
def reset():
    return {"message": "reset successful"}

@app.post("/step")
def step(action: dict):
    return {"result": "step executed"}

@app.post("/predict")
def predict(data: dict):
    return {"prediction": "dummy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
  
 
