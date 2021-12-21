test:
	flake8
	mypy game_objects
	python -m pytest ./tests

