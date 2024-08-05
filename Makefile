lint:
	ruff check .
	ruff format .

deploy: lint
	pyinstaller qtformatkit.spec
