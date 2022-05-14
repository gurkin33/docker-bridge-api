# Docker container bridge to host via API

It is required, when you have to execute several commands on host PC, to manage output in container.

## Two APIs here

- API in Docker container
- API on host PC/serve (bridge-app)

## To run bridge-app

```zsh
export FLASK_APP=bridge_app.py

flask run --host 0.0.0.0 --port 5001
```

## To run docker container

```zsh
cd docker-image
docker-compose up -d
```
