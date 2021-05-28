FROM python:3.9.5-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run"]