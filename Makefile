.PHONY:build shell
build:
	docker-compose build pg_workshop
shell: build
	docker-compose run --rm --service-ports pg_workshop /bin/bash
