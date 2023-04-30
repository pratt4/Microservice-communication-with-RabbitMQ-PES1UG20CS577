FROM python:3.8-slim-buster

WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY consumer3.py consumer3.py

CMD ["python3", "consumer3.py"]

