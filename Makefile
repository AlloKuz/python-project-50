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

