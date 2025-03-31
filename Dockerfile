FROM python:3.11.9

WORKDIR /app

COPY poe

RUN make install

COPY . .

COPY .env .env