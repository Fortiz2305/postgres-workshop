.PHONY:build shell test clean
build:
	docker-compose build
shell: build
	docker-compose up -d db
	docker-compose run --rm --service-ports pg_workshop /bin/bash

test: build
	docker-compose run --rm pg_workshop bash -c 'pytest tests/'


clean:
	docker-compose stop && docker-compose rm --all -f
