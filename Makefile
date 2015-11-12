.PHONY: clean install flake8 test update_tlds

clean:
	@echo 'Cleaning .pyc and __pycache__ files'
	$(shell find . -name "*.pyc" -delete)
	$(shell find . -name "__pycache__" -delete)
	$(shell find . -name ".cache" -exec /bin/rm -r {} +;)

install: clean
	pip install -r requirements.txt --allow-all-external

update_tlds: clean
	@echo 'Updating tlds from http://data.iana.org/TLD/tlds-alpha-by-domain.txt'
	python update_tlds.py

flake8: clean
	flake8 .

test: clean flake8
	coverage run --source urlreplacer -m py.test tests/
	coverage report -m
