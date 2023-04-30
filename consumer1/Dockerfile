FROM python:3.8-slim-buster

WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY consumer1.py consumer1.py

CMD ["python3", "consumer1.py"]

