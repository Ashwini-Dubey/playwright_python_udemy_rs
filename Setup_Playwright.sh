#!/usr/bin/env zsh
# Installation of Python
echo "Install Python"
brew install python

echo "Checking Python Version"
python3 --version

echo "Running pip from CLI"
python3 -m pip3 --version

echo "Upgrade pip"
python3 -m pip3 install --upgrade pip

echo "Create virtual environment"
python3 -m venv automation_env
source automation_env/bin/activate

echo "Install pytest framework"
python3 -m pip3 install pytest

echo "Install Playwright for Python"
pip3 install pytest-playwright

echo "Install the required browsers"
playwright install


