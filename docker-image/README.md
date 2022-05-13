# Docker flask app

## To run flask locally:
flask run --host 0.0.0.0 --port 9000

## To run container use command below

docker run --rm -p 8080:9000 -d --name replic-app -v "/Users/alex...:/replic-app" -v /replic-app/venv -v /replic-app/__pycache__ replic-manager:latest