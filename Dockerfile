# Use a python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
# This will copy inference.py and the src/ folder into /app/
COPY . .

# Set the command to run the file now located at the root
CMD ["python", "inference.py"]
# ... (rest of your Dockerfile)
COPY . .
CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "80"]
