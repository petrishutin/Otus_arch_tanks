test:
	flake8
	mypy game/game_objects.py
	python -m pytest ./tests

