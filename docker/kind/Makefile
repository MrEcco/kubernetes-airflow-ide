DOCKER_IMAGE=local/kind:local
DOCKERFILE=./Dockerfile

build:
	@docker build --compress --pull -f $(DOCKERFILE) -t $(DOCKER_IMAGE) .
