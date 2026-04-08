FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn

EXPOSE 7860

CMD ["python", "inference.py"]
