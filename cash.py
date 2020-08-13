# Program to determine amount of coins needed to make change from cash transaction

from math import floor


def main():

    # Ask for change amount
    while True:
        change = get_float("Change owed: ")
        if change > 0:
            break

    # Declare variables
    coins = 0

    # Check for number of quarters
    if change >= 0.25:
        coins, change = change_maker(change, coins, 0.25)

    # Check for number of dimes
    if change >= 0.10:
        coins, change = change_maker(change, coins, 0.10)

    # Check for number of nickels
    if change >= 0.05:
        coins, change = change_maker(change, coins, 0.05)

    # Check for number of pennies
    if change <= 0.04:
        coins, change = change_maker(change, coins, 0.01)

    # Print coins
    print(coins)

# Make change for each coin value


def change_maker(change, coins, value):
    coin = floor(change / value)
    change = change - (value * coin)
    coins = coins + coin
    return coins, round(change, 2)


main()
