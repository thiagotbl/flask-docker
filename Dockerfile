FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install python-pip -y && \
    pip install -U pip

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src ./src

CMD ["python", "src/app.py"]
