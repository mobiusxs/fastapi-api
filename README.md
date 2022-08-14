# FastAPI API

Example API using FastAPI with SQLAlchemy and SQLAlchemy-Mixins

## Quickstart

1. Install dependencies

    ```
    python -m venv venv
    pip install -r requirements.txt
    ```

2. Set environment variables

    ```
    DATABASE_URL=sqlite:///db.sqlite3
    ```

3. Initialize database

    ```
    alembic -c alembic/alembic.ini revision --autogenerate
    alembic -c alembic/alembic.ini upgrade head
    ```

1. Run

    ```
    uvicorn api:app --host localhost --port 80 --reload
    ```

1. Interact with Swagger UI

    http://localhost

## Docker

1. Build and run

    ```
    docker build -t api .
    docker run -d -p 80:5000 -e "DATABASE_URL=sqlite:///db.sqlite3" --name api api
    ```

1. Initialize database

    ```
    docker exec -it api bash
    alembic -c alembic/alembic.ini revision --autogenerate
    alembic -c alembic/alembic.ini upgrade head
    exit
    ```

1. Teardown

    ```
    docker stop api
    docker rm api
    docker image rm api
    ```

## Docker Compose

1. Build and run

    ```
    docker compose up -d
    ```

1. Initialize database

    ```
    docker exec -it api bash
    alembic -c alembic/alembic.ini revision --autogenerate
    alembic -c alembic/alembic.ini upgrade head
    exit
    ```

1. Teardown

    ```
    docker compose down
    docker image rm api
    ```
