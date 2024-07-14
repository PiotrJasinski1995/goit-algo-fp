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
    
    print_probabilities_table(sum_dict, num_experiments)


def print_probabilities_table(data, number_of_experiments):
    # create header
    head = ['Sum', 'Probability']

    percent_data = {item: f'{round((data[item] / float(num_experiments)) * 100, 2)}% ({data[item]}/{num_experiments})' for item in data}

    # display table
    print(f'\nFor {number_of_experiments} experiments:')
    print(tabulate(percent_data.items(), headers=head, tablefmt="grid"))


# Theoretical data
num_experiments = 36
sum_dict = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
print("THEORETICAL DATA:")
print_probabilities_table(sum_dict, num_experiments)

print("\nEXPERIMENTAL DATA:")
num_experiments = 36
monte_carlo_simulation(num_experiments)

num_experiments = 15000
monte_carlo_simulation(num_experiments)
