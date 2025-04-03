FROM python:3.11.9

WORKDIR /app

COPY pyproject.toml pyproject.toml

RUN make install

COPY . .

COPY .env .env
