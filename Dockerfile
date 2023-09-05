FROM python:3.8-slim-buster

RUN apt update -y && \
    apt install libgl1-mesa-glx -y && \
    apt install libglib2.0-0 -y

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]