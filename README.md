# MLS API

This project provides CRUD operations on a MLS API.

The project implements FastAPI web framework running on Uvicorn.
Database operations are performed over Tortoise ORM.


## Run Locally

You must have Docker pre-installed.

Clone the project

```bash
  git clone https://github.com/doluca/mls-api
```

Go to the project directory

```bash
  cd mls-api
```

Run on Docker

```bash
  docker-compose up -d
```

## Docs & playground

[http://localhost:8008/docs](http://localhost:8008/docs)

## Running Tests

To run tests, run the following command

```bash
  docker exec mls-web pytest
```
