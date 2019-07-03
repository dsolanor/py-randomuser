test:
	python -m pytest -v --disable-warnings --cov=randomuser ./tests

gitignore:
	curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
