.DEFAULT_GOAL := build

.PHONY: build
build:
	ansible-builder build --container-runtime=docker --tag quay.io/mamercad/ansible-ee:ee1

.PHONY: push
push:
	docker push quay.io/mamercad/ansible-ee:ee1
