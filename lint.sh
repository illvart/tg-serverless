#!/usr/bin/env bash
set -e

find . -name "*.py[co]" -o -name __pycache__ -exec rm -rf {} +
#rm -rf .mypy_cache

echo "> isort"
isort --gitignore --settings-file=setup.cfg .
echo "> brunette"
brunette --config=setup.cfg .
echo "> flake8"
flake8 --config=setup.cfg .
echo "> mypy"
mypy --config-file=setup.cfg .
echo "> prettyjson"
python3 -m scripts.prettyjson
