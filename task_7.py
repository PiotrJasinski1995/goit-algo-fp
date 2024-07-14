import random
from tabulate import tabulate


def monte_carlo_simulation(num_experiments):
    # Performs a series of Monte Carlo simulations
    sum_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    probabilities_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    for _ in range(num_experiments):
        # Generate random points
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        sum = dice_1 + dice_2

        sum_dict[sum] += 1

    for sum in probabilities_dict:
        probability = round((sum_dict[sum] / float(num_experiments)) * 100, 2)
        probabilities_dict[sum] = f'{probability}% ({sum_dict[sum]}/{num_experiments})'
    
    # create header
    head = ['Sum', 'Probability']

    # display table
    print(f'\nFor {num_experiments} experiments:')
    print(tabulate(probabilities_dict.items(), headers=head, tablefmt="grid"))


num_experiments = 15000
monte_carlo_simulation(num_experiments)

num_experiments = 36
monte_carlo_simulation(num_experiments)
