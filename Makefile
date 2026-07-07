run:
	uvicorn backend.main:app --reload

test:
	pytest

lint:
	ruff check .

format:
	black .

typecheck:
	mypy backend