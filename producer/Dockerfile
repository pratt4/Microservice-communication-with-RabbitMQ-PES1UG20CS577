FROM python:3.8-slim-buster

WORKDIR /application

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py

RUN mkdir static
RUN mkdir static/css
COPY static/css/main.css static/css/main.css

RUN mkdir templates
COPY templates/index.html templates/index.html
COPY templates/base.html templates/base.html
COPY templates/view_records.html templates/view_records.html

EXPOSE 5000

CMD ["python3", "app.py"]

