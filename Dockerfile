FROM python:3.10-slim

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./application .
COPY docker_config.py default_config.py

CMD ["python", "app.py"]

