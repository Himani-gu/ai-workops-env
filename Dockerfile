# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /workspace

# Copy project files
COPY requirements.txt .
COPY inference.py .
# Copy other project files if needed
COPY app/ ./app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command for testing
CMD ["python", "inference.py"]
