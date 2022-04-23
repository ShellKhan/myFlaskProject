FROM python:3.9.5-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT flask run --host=0.0.0.0