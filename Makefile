install:
	poetry install

	
gendiff:
	@poetry run gendiff


build:
	poetry build


package-install:
	pip install --user dist/*.whl


lint:
	poetry run flake8 gendiff


test:
	poetry run pytest tests -vv


coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/