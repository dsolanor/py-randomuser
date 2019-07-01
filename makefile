test:
	python -m pytest --disable-warnings --cov=tidebot ./tests

gitignore:
	curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
