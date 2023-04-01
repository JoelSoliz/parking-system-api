CONTAINER_NAME?=parking-system
CMD?=bash

export UID=$(shell id -u)

setup:
	pip install pre-commit
	pre-commit install

rebuild:
	docker compose build

build:
	docker compose build --no-cache

up:
	docker compose up --detach

start: up
	docker compose exec -u $(UID) $(CONTAINER_NAME) uvicorn parking_system.main:app --host 0.0.0.0 --reload

test: up
	docker compose exec -u $(UID) $(CONTAINER_NAME) pytest

shell: up
	docker compose exec -u $(UID) $(CONTAINER_NAME) $(CMD)

clean: clean-pyc
	docker compose down

clean-pyc:
	find . -type d -name '__pycache__' -exec rm -rf {} \; || exit 0
	find . -type f -iname '*.pyc' -delete || exit 0
