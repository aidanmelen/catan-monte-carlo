# A monte carlo simuation of card stack: dice mode

import pandas as pd

import random
import os


NUMBER_OF_ROLLS = 10000


def generate_dice_mode_card_stack():
    """Generate a new dice mode card stack list."""

    # two virtual card stacks containing 36 cards each are generated
    card_stack_1 = [
        2,
        3, 3,
        4, 4, 4, 
        5, 5, 5, 5,
        6, 6, 6, 6, 6,
        7, 7, 7, 7, 7, 7,
        8, 8, 8, 8, 8,
        9, 9, 9, 9,
        10, 10, 10,
        11, 11,
        12
    ]
    card_stack_2 = card_stack_1.copy()

    # 18 cards are removed from each stack at random.
    for i in range(0, 18):
        removal_index = random.randint(0, len(card_stack_1) - 1)
        del card_stack_1[removal_index]

    for i in range(0, 18):
        removal_index = random.randint(0, len(card_stack_2) - 1)
        del card_stack_2[removal_index]

    # The remaining cards are suffled into a new 36-card stack.
    # Now, this is the card stack used for the game.
    card_stack = card_stack_1 + card_stack_2
    random.shuffle(card_stack)

    return card_stack

print(f"Running dice mode with {NUMBER_OF_ROLLS} rolls.")

results = {}
count = 0
while count < NUMBER_OF_ROLLS:

    random_rolls_in_game = random.randint(50, 100)
    for i in range(0, random_rolls_in_game):
        # start of a new game
        card_stack = generate_dice_mode_card_stack()

        while card_stack:
            # draw a card from the top of the card stack
            roll = card_stack.pop()
            count += 1

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

df.to_csv(f'results/dice-mode-{NUMBER_OF_ROLLS}.csv', index = True)