.PHONY: init
init:
	pip install -r requirements.txt

.PHONY: lint
lint:
	pylint cast_compare

.PHONY: test
test:
	python -m unittest discover tests
