test:
	python -m pytest -rXs -vv --cov-report term-missing --cov=randomuser tests

gitignore:
	curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore

build:
	python setup.py build bdist_wheel

install:
	python setup.py install