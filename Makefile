.DEFAULT_GOAL := error
.PHONY: build publish package coverage test lint docs venv
PROJ_SLUG = chopit
CLI_NAME = chopit
LINTER = pylint
SHELL = bash


error:
	@echo "please select a target"

build:
	pip install --editable .

run:
	$(CLI_NAME) run

submit:
	$(CLI_NAME) submit

freeze:
	pip freeze > requirements.txt

lint:
	$(LINTER) $(PROJ_SLUG)

test: lint
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

quicktest:
	py.test --cov-report term --cov=$(PROJ_SLUG) tests/

coverage: lint
	py.test --cov-report html --cov=$(PROJ_SLUG) tests/


package: clean docs
	python setup.py sdist

publish: package
	twine upload dist/*

clean :
	rm -rf dist \
	rm -rf docs/build \
	rm -rf *.egg-info
	coverage erase

venv :
	python3 -m venv venv
	source venv/bin/activate && pip install pip --upgrade --index-url=https://pypi.org/simple
	source venv/bin/activate && pip install -r requirements_dev.txt
	source venv/bin/activate && pip install --editable .

install:
	pip install -r requirements_dev.txt

licenses:
	pip-licenses --with-url --format=rst \
	--ignore-packages $(shell cat .pip-lic-ignore | awk '{$$1=$$1};1')
