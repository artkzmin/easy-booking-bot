install:
	poetry install

run:
	poetry run python src/main.py

test:
	poetry run pytest -v 