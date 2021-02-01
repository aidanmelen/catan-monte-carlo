# A monte carlo simulation of random number generation

import pandas as pd

import random
import os

NUMBER_OF_ROLLS = 10000


print(f"Running rng mode with {NUMBER_OF_ROLLS} rolls.")

results = {}
for i in range(0, NUMBER_OF_ROLLS):

    # generate two random dice rolls
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    roll = r1 + r2

    # record result
    if roll in results:
        results[roll] += 1
    else:
        results[roll] = 1

print(results)
df = pd.DataFrame.from_dict(results, orient="index")
df.sort_index(inplace=True)

if not os.path.exists('results'):
    os.makedirs('results')

df.to_csv(f'results/rng-mode-{NUMBER_OF_ROLLS}.csv', index = True)
