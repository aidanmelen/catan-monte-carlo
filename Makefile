NAME = catan-monte-carlo

all :: build run

build ::
	# Build release image.
	docker build . -t $(NAME)

dev :: build
	# Run the developer workspace.
	docker run -v "$$(pwd)":/app --entrypoint /bin/bash --rm -it $(NAME)

run ::
	# Run container.
	docker run -v "$$(pwd)/results":/app/results --rm $(NAME)

clean ::
	# Delete results
	@rm -rf results/*

	# Delete python cache files
	@rm -rf build dist .eggs *.egg-info .venv
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +