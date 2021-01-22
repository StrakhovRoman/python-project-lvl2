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
