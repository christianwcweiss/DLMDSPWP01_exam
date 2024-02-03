clean_setup:
	# Python
	pyenv install -s $(shell cat .python-base-version)
	pyenv virtualenv-delete -f $(shell cat .python-version) || true
	pyenv virtualenv $(shell cat .python-base-version) $(shell cat .python-version)
	make setup
	pyenv version

setup:
	pip install -r requirements.txt
