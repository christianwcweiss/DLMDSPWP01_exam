# DLMDSPWP01_exam

## Local Setup (Tested on MacOSX)

### Brew
If not already installed, get the package manager here: https://brew.sh/
``` shell script
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### Python
Install [pyenv](https://github.com/pyenv/pyenv) and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
``` shell
brew install pyenv
brew install pyenv-virtualenv
```
Make sure to properly configure your terminal so that `which python` points to some `pyenv` shim file.
Probably you need to add the following two lines to your `~/.bashrc`/`~/.zshrc` file:
``` shell
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Activate your terminal config:
```source ~/.zshrc``` or ```source ~/.bashrc```

In the project root folder execute:
``` shell
make clean_setup
```

## Code Quality Checks

I use [black](https://black.readthedocs.io/en/stable/) as auto-formatter.
Make sure to always format your code e.g. with `black -l 120` for Python.
Linting is done via `flake8`.
Our type checker can be run with `pre-commit run mypy -a` (see next step).

To setup a shared [pre-commit](https://pre-commit.com/) hook (configured via _.pre-commit-config.yaml_), just run
```
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit install --hook-type prepare-commit-msg
```
in this repository.
