import numpy as np
import pandas as pd
import re

score = 0
data = pd.read_csv('african_countries.csv', names=['Country', 'Capital'])
size = len(data['Country'])
rand = []

for index in range(10):
    random_number = np.random.randint(size - 1)  # implies random integer from 0-54 since size=55

    while True:
        # to avoid repeated random numbers
        if random_number in rand:
            random_number = np.random.randint(size - 1)
        else:
            rand.append(random_number)
            break

    country = data['Country'][random_number]
    capital = data['Capital'][random_number]
    capital = capital.strip()

    # question
    capital_input = input(f'What is the capital of {country}?: ')
    capital_input = capital_input.strip()

    if '*' in capital:
        capital = capital.split("*")
        for any_capital in capital:
            if capital_input.lower() == any_capital.lower().strip():
                score += 5
                print("correct")
                print("score: " + str(score))
                break
            else:
                score += 0
                print("Incorrect")
                print("score: " + str(score))
    else:
        if capital_input.lower() == capital.lower():
            score += 5
            print("correct")
        else:
            score += 0
            print("Incorrect")

# game ends
print(f'\n\tYou scored: ' + str(score) + " points")

