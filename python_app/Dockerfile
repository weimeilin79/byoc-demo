# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app .
CMD ["python", "main.py"]
