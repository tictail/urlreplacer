.PHONY: clean install flake8 test

clean:
	@echo 'Cleaning .pyc and __pycache__ files'
	$(shell find * -name "*.pyc" -delete)
	$(shell find * -name "__pycache__" -delete)

install: clean
	pip install -r requirements.txt --allow-all-external

flake8: clean
	flake8 .

test: clean flake8
	coverage run --source tokenize -m py.test tests/
	coverage report -m
