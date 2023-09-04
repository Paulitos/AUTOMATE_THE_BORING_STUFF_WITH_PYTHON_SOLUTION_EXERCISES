# Coin Flip Streaks Page 107 Chapter 4
import random

numberOfStreaks = 0
streak_length = 6
num_experiments = 10000

for experimentNumber in range(num_experiments):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coin_flips = ''.join(random.choice(['H', 'T']) for _ in range(100))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(len(coin_flips) - streak_length + 1):
        if len(set(coin_flips[i:i+streak_length])) == 1:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / num_experiments))

