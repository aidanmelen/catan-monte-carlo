# A Monte Carlo simulation of random number generator (RNG)
import click
import random
import helpers


def run(number_of_rolls):
    """Run the rolls for the RNG simulation."""
    rolls = {}
    for i in range(0, number_of_rolls):

        # generate two random dice rolls
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        roll = r1 + r2

        # record roll
        if roll in rolls:
            rolls[roll] += 1
        else:
            rolls[roll] = 1
    
    return rolls


@click.command()
@click.option("rolls", "--rolls", "-r", default=100, show_default=True, help="The number of rolls used in the simulation.")
@click.option("write_csv", "--write-csv", "-w", is_flag=True, help="Write dataframe to CSV file.")
@click.option("write_chart", "--write-chart", "-wc", is_flag=True, help="Write chart to file.")
@click.option("plot_chart", "--plot-chart", "-pc", is_flag=True, help="Plot chart.")
def main(rolls, write_csv, write_chart, plot_chart):
    """The main entrypoint."""
    print(f"Running RNG mode with {rolls} rolls.\n")
    data = run(rolls)
    df = helpers.get_df(data)

    print(df.to_string(index=False))

    if write_csv:
        helpers.write_csv(df, 'rng', rolls)

    if write_chart:
        helpers.write_chart(df, 'rng', rolls)

    if plot_chart:
        helpers.plot_chart(df)


if __name__ == "__main__":
    main()