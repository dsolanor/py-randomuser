test:
	python -m pytest --disable-warnings --cov=randomuser ./tests && radon cc -s randomuser/* path

gitignore:
	curl https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore > .gitignore
