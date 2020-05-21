FROM python:3.8.3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src ./src

CMD ["python3", "-u", "src/app.py"]
