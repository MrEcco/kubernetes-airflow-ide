DOCKER_IMAGE=local/airflow:local
DOCKERFILE=./Dockerfile

build:
	@docker build --compress --pull -f $(DOCKERFILE) -t $(DOCKER_IMAGE) .
