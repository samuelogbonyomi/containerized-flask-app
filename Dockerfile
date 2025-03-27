# Use the official Python 3.8 slim image as the base image
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
#Install dependedncies
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "app.py"]
