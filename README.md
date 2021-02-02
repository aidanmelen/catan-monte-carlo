# catan-monte-carlo

Compare similiations of RNG and Card stack: dice mode from Catan Universe.

## Usage

Build the docker image.

```bash
make build
```

Get a development shell in the container.

```bash
make dev
```

Run the docker container.

```bash
make run
```

## Results

| Number Of Rolls | RNG Mode                                  | Dice Mode                                 |
|-----------------|-------------------------------------------|-------------------------------------------|
| 25              | ![25](results/png/rng-mode-25.png)        | ![25](results/png/dice-mode-25.png)       |
| 50              | ![50](results/png/rng-mode-50.png)        | ![50](results/png/dice-mode-50.png)       |
| 75              | ![75](results/png/rng-mode-75.png)        | ![75](results/png/dice-mode-75.png)       |
| 100             | ![100](results/png/rng-mode-100.png)      | ![100](results/png/dice-mode-100.png)     |
| 1000            | ![1000](results/png/rng-mode-1000.png)    | ![1000](results/png/dice-mode-1000.png)   |
| 5000            | ![5000](results/png/rng-mode-5000.png)    | ![5000](results/png/dice-mode-5000.png)   |
| 10000           | ![10000](results/png/rng-mode-10000.png)  | ![10000](results/png/dice-mode-10000.png) |