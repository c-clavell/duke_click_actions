install:
	python -m pip install --upgrade pip &&\
	python -m pip install -r requirements.txt

test:
	python -m pytest -vv clickFiles/tests/test_click1.py

format:
	black *.py

lint:
	pylint --disable=R,C clickFiles/click1.py

all: install lint test