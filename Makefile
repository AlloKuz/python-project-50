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

# Dev
dev:
	poetry install --with dev

lint: dev
	poetry run flake8 gendiff

test-coverage: dev
	poetry run pytest --cov=gendiff --cov-report xml

show-coverage: dev
	poetry run pytest --cov=gendiff --cov-report term-missing

test: dev
	poetry run pytest


.PHONY: install lint test publish gendiff dev