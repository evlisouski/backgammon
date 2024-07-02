COMPOSE_FILE = docker-compose.yml
TESTS_PATH = src/tests

 
.PHONY: up stop down rm test

up:	test
	docker compose -f $(COMPOSE_FILE) up -d
	@sleep 5
	@if curl http://127.0.0.1:8000/health_check | grep -q 'OK'; then \
		echo "The application is up and working!"; \
	else \
		echo "The application is not responding!"; \
	fi

stop:
	docker compose -f $(COMPOSE_FILE) stop

down:
	docker compose -f $(COMPOSE_FILE) down

rm:
	docker compose -f $(COMPOSE_FILE) down --volumes --remove-orphans
	docker rmi -f $(shell docker images backgammon -q)

test:
	@if pytest $(TESTS_PATH) | grep -q 'failed'; then \
		echo "Tests failed. Aborting."; \
		exit 1; \
	else \
		echo "Tests passed"; \
	fi
