def greedy_algotithm(money_given, items):
    money_sum = money_given
    budget_possible = True
    sorted_items = dict(sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True))
    dish_list = []
    ratio_sum = 0
    
    while budget_possible:
        current_item = list(sorted_items.keys())[0]
        current_dish_value = sorted_items[current_item]['cost']

        if money_sum >= current_dish_value:
            money_sum -= current_dish_value
            dish_list.append(current_item)
            ratio_sum += sorted_items[current_item]['calories'] / sorted_items[current_item]['cost']
            sorted_items.pop(current_item)
        else:
            budget_possible = False
    
    print('\nGreedy algorithm:')
    print(f'For the {money_given} we can get:\n{dish_list}\nto get best ratio of calories to cost.\nRatio sum: {ratio_sum:.2f}, money left: {money_sum}.')


def dynamic_programming(money_given, items):
    dish_list = []
    item_list = list(items.keys())

    # calories list
    val = [items[item]['calories'] for item in items]

    # cost list
    wt = [items[item]['cost'] for item in items]
    n = len(val)

    # create a table K to store the optimal values of the subtasks
    K = [[0 for w in range(money_given + 1)] for i in range(n + 1)]

    # build table K from the bottom up
    for i in range(n + 1):
        for w in range(money_given + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    
    i = n
    money = money_given
    calories_sum = K[n][money_given]

    while (i > 0):
        if (K[i][money] != K[i - 1][money]):
            dish_list.append(item_list[i - 1])
            money -= wt[i - 1]
        
        i -= 1

    print('\nDynamic programming algorithm:')
    print(f'For the {money_given} we can get:\n{dish_list} to maximize calorie content.\nCalories: {calories_sum}, money left: {money}.')


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

money = 100
greedy_algotithm(money, items)
dynamic_programming(money, items) # 220
