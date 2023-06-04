up:
	 docker compose up

up-with-build:
	 docker compose up --build

up-with-debug-mode:
	 docker-compose run --rm --service-ports backend
