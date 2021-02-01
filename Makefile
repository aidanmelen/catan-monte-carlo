NAME = catan-monte-carlo

build ::
	# Build release image.
	docker build . -t $(NAME)

dev :: build
	# Run the developer workspace.
	docker run -v "$$(pwd)":/app --entrypoint /bin/bash --rm -it $(NAME)

run ::
	# Run container.
	docker run -v "$$(pwd)/results":/app/results --rm $(NAME)
