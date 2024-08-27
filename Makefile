install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --break-system-packages --force-reinstall

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test:
	poetry run pytest

show-coverage:
	poetry run pytest --cov=gendiff --cov-report term-missing


.PHONY: install lint test publish gendiff