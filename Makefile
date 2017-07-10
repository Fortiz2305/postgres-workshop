.PHONY:build shell
build:
	docker-compose build
shell: build
	docker-compose up -d db
	docker-compose run --rm --service-ports pg_workshop /bin/bash

clean:
	docker-compose stop && docker-compose rm --all -f
