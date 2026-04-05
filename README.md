# fastapi-sandbox

Sandbox for playing around with FastAPI

## Local Dev

### Docker Setup

You should be able to run the environment in a container. You just need to have Docker installed and then you can try running the following to get started.

#### To watch for changes

```
docker compose watch
```

#### To start the container

```
docker compose up
```

After that completes you can just navigate to http://localhost.

#### Running tests

We run `pytest` in the fastapi-server since it is configured properly with all Postgresql environment variables.

```
docker exec -it fastapi-server pytest
```

### Local Setup

#### Set up a new virtual environment (optional)

You will be installing some new Python requirements, so it's recommended to get a virtual environment set up.

```
python -m venv .venv
```

#### Install Requirements

The typical `pip install` will help you get set up.

```
pip install -r requirements.txt
```

#### Running fastapi

After installing the requirements, `fastapi` should be available to run in a shell. Run the following to run fastapi in development mode.

```
fastapi dev src/main.py
```
