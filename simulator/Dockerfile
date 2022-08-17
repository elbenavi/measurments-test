FROM python:3.10.6

WORKDIR /app

COPY requirements.txt .

COPY main.py .

RUN python -m pip install -r requirements.txt

CMD ["python", "main.py"]
