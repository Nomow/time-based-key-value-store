# Time Based Key-Value Store


[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![postgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

[![Open Issues](https://img.shields.io/github/issues-raw/Nomow/time-based-key-value-store?style=for-the-badge)](https://github.com/Nomow/time-based-key-value-store/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/Nomow/time-based-key-value-store?style=for-the-badge)](https://github.com/Nomow/time-based-key-value-store/issues?q=is%3Aissue+is%3Aclosed)
[![Open Pulls](https://img.shields.io/github/issues-pr-raw/0xTheProDev/fastapi-clean-example?style=for-the-badge)](https://github.com/Nomow/time-based-key-value-store/pulls)
[![Closed Pulls](https://img.shields.io/github/issues-pr-closed-raw/Nomow/time-based-key-value-store?style=for-the-badge)](https://github.com/Nomow/time-based-key-value-store/pulls?q=is%3Apr+is%3Aclosed)
[![Contributors](https://img.shields.io/github/contributors/Nomow/time-based-key-value-store?style=for-the-badge)](https://github.com/Nomow/time-based-key-value-store/graphs/contributors)
[![Activity](https://img.shields.io/github/last-commit/Nomow/time-based-key-value-store?style=for-the-badge&label=most%20recent%20activity)](https://github.com/Nomow/time-based-key-value-store/pulse)

## Description
Time Based Key-Value Store Application using FastAPI framework in Python 3 with PostgreSQL.

Store multiple values for the same key at different timestamps and retrieve the keys value at a certain timestamp with persistent storage in PostgreSQL.

## Running the application
### Using  [Docker Compose](https://docs.docker.com/compose/)

- Run the command from command prompt to create and start containers:
  ```sh
  $ docker-compose up
  ```

- Run the command from command prompt to stop and remove containers, networks:
  ```sh
  $ docker-compose down
  ```

- Open `localhost:8000/docs` for API Documentation. **Note:** Swagger UI doesn't support get request with payload [(See the swagger UI issue)](https://github.com/swagger-api/swagger-ui/issues/2136)

## Curl example

- Run the following curl command in terminal for PUT request:
  ```sh
  $ curl -X PUT http://localhost:8000 -H 'Content-Type: application/json' -d '{"key": "mykey", "value": "abc", "timestamp" : 143111}' -i
  ```
- Run the following curl command in terminal for GET request:
  ```sh
  $ curl -X GET http://localhost:8000 -H 'Content-Type: application/json' -d '{"key": "mykey", "timestamp" : 143111}' -i
  ```

## Installation
**Note:** use `poetry version 1.3.2`, due to `psycopg2` issues.
#### PostgreSQL database
  ```sh
  $ docker run -d -e POSTGRES_PASSWORD=test123 -p 5432:5432 postgres
  ```

### Poetry
Run the following commands in terminal
  ```sh
  $ pip3 install poetry==1.3.2
  $ poetry lock --no-update
  $ poetry install
  $ poetry run uvicorn app.main:app
  ```
## Testing
- Testing with PyTest:

  ```sh
  $ pytest
  ```
- To include Coverage Reporting as well:
  ```sh
  $ pytest --cov
  ```

