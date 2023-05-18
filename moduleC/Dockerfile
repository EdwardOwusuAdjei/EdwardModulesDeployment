FROM python:3.8-slim-buster

WORKDIR /app

ADD . /app

RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

CMD ["python", "main.py"]