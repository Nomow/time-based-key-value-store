FROM python:3.11-slim-buster

EXPOSE 8000
WORKDIR /app

RUN apt-get update
RUN apt-get -y install libpq-dev gcc && pip install psycopg2

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip
RUN pip install poetry==1.3.2

RUN poetry lock --no-update
RUN poetry install

COPY . ./

CMD poetry run uvicorn --host=0.0.0.0 app.main:app