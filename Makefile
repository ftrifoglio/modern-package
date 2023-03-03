SHELL = /bin/bash
VENV_DIR = .venv
POETRY_DIR = .poetry
PYTHON = $(VENV_DIR)/bin/python
POETRY = $(POETRY_DIR)/bin/poetry
PIP = $(POETRY_DIR)/bin/pip
PRE-COMMIT = $(VENV_DIR)/bin/pre-commit
PYTEST = $(VENV_DIR)/bin/pytest
GENBADGE = $(VENV_DIR)/bin/genbadge
# COLOURS
COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

.DEFAULT_GOAL = help

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; \
	printf "\nUsage: make\n\nTargets:\n"} \
	/^[a-zA-Z_-]+:.*?##/ \
	{ printf "$(COLOUR_BLUE)%-15s$(COLOUR_END) %s\n", $$1, $$2 }' \
	$(MAKEFILE_LIST)

.python-version:
	@brew upgrade pyenv --quiet
	@pyenv install 3.11 --skip-existing
	@pyenv install 3.10 --skip-existing
	@pyenv install 3.9 --skip-existing
	@pyenv install 3.8 --skip-existing
	@pyenv local 3.11 3.10 3.9 3.8

$(POETRY_DIR):
	@python -m venv $(POETRY_DIR)
	@$(PIP) install pip --upgrade --quiet
	@$(PIP) install wheel --quiet
	@$(PIP) install poetry==1.2.1 --quiet

$(VENV_DIR): $(POETRY_DIR)
	@$(POETRY) install --no-interaction --with=dev,tests,docs

.git/hooks/commit-msg: $(VENV_DIR)
	@if [ -f $(PRE-COMMIT) ]; then \
		$(PRE-COMMIT) install --hook-type commit-msg; \
	fi

.git/hooks/pre-commit: $(VENV_DIR)
	@if [ -f $(PRE-COMMIT) ]; then \
		$(PRE-COMMIT) install --hook-type pre-commit; \
	fi

.git/hooks/pre-push: $(VENV_DIR)
	@if [ -f $(PRE-COMMIT) ]; then \
		$(PRE-COMMIT) install --hook-type pre-push; \
	fi

.PHONY = _venv venv

_venv: .python-version \
	$(VENV_DIR) \
	.git/hooks/commit-msg \
	.git/hooks/pre-commit \
	.git/hooks/pre-push

venv: _venv ## Create virtual environment

reports: ## Create tests and coverage reports
	@mkdir -p reports/coverage/coverage-html
	@mkdir -p reports/junit
	@$(PYTEST) --junitxml=reports/junit/junit.xml \
		--html=reports/junit/report.html \
		--cov-report xml:reports/coverage/coverage.xml \
		--cov-report html:reports/coverage/coverage-html \
		--cov=package \
		tests/
	@$(GENBADGE) tests --output-file=reports/junit/junit-badge.svg
	@$(GENBADGE) coverage --output-file=reports/coverage/coverage-badge.svg
	@rm -f .coverage
	@rm -f reports/coverage/coverage-html/.gitignore

.PHONY = html_doc

html_doc: ## Create HTML documentation
	@rm -rf docs/build
	@rm -rf docs/_autosummary
	@cd docs && make html
	@open docs/build/html/index.html

.PHONY = clean

clean: ## Clean up environment
	@rm -rf $(VENV_DIR)
	@rm -rf $(POETRY_DIR)
	@rm -rf ./.tox
	@rm -rf ./reports
	@rm -rf ./dist
	@rm -rf ./docs/build
	@rm -rf ./docs/_autosummary
	@rm -f .git/hooks/commit-msg
	@rm -f .git/hooks/pre-commit
	@rm -f .git/hooks/pre-push
	@rm -f poetry.lock
	@rm -f .coverage
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@rm -f .python-version
	@find . | grep __pycache__ | xargs rm -rf
	@find . | grep .ipynb_checkpoints | xargs rm -rf
	@find . | grep token.json | xargs rm -rf
