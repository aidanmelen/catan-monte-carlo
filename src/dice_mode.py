# A Monte Carlo simuation of card stack: dice mode
import click
import random
import helpers


def create_card_stack():
    """Create a new card stack list."""
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


def run(number_of_rolls):
    """Run the rolls for the simulation."""
    rolls = {}
    card_stack = []
    count = 0
    while True:

        # randomize the number of rolls in a game
        rolls_in_game = random.randint(50, 100)

        for i in range(0, rolls_in_game):
            # create a new card stack for each new game
            
            if not card_stack:
                card_stack = create_card_stack()

            while card_stack:
                # draw a card from the top of the card stack
                roll = card_stack.pop()
                count += 1

                # record result
                if roll in rolls:
                    rolls[roll] += 1
                else:
                    rolls[roll] = 1
                
                # break inner while loop
                if count > number_of_rolls:
                    break

            # break inner for loop
            if count > number_of_rolls:
                break
        
        # break outter while loop
        if count > number_of_rolls:
            break
                    
    return rolls


@click.command()
@click.option("rolls", "--rolls", "-r", default=100, show_default=True, help="The number of rolls used in the simulation.")
@click.option("write_csv", "--write-csv", "-w", is_flag=True, help="Write dataframe to CSV file.")
@click.option("write_chart", "--write-chart", "-wc", is_flag=True, help="Write chart to file.")
@click.option("plot_chart", "--plot-chart", "-pc", is_flag=True, help="Plot chart.")
def main(rolls, write_csv, write_chart, plot_chart):
    """The main entrypoint."""
    print(f"Running dice mode with {rolls} rolls.\n")
    data = run(rolls)
    df = helpers.get_df(data)

    print(df.to_string(index=False))

    if write_csv:
        helpers.write_csv(df, 'dice', rolls)

    if write_chart:
        helpers.write_chart(df, 'dice', rolls)

    if plot_chart:
        helpers.plot_chart(df)


if __name__ == "__main__":
    main()