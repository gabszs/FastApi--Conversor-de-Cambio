FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/"

COPY ./poetry.lock /
COPY ./pyproject.toml /
COPY ./.env /

RUN apt-get update -y && apt-get install curl -y \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install --no-root \
    && apt-get remove curl -y

ADD . /app

WORKDIR /app

EXPOSE 5000

CMD ["python", "main.py"]
