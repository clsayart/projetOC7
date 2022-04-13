from time import time
from os import path, remove

import csv

time_debut = time()

# with open("files/dataset1_Python+P7.csv", 'r') as file:
# with open("files/dataset2_Python+P7 - Copie.csv", 'r') as file:
# with open("files/actions_with_benefits.csv", 'r') as file:

rows = []
with open("files/actions_with_benefits.csv", 'r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        rows.append(row)
# print("header", header)
# print("rows", rows)

clean_rows_dyn = []
for row in rows:
    if float(row[1]) > 0 and float(row[2]) > 0:  # remove null or negative values
        clean_rows_dyn.append((row[0], float(row[1]), float(row[2])))

print('clean rows opti', clean_rows_dyn)


def algo_dynamic(budget, actions):
    matrice = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]

    for i in range(1, len(actions) + 1):
        for w in range(1, budget + 1):
            if actions[i - 1][1] <= w:
                matrice[i][w] = max(actions[i - 1][2] + matrice[i - 1][int(w - actions[i - 1][1])], matrice[i - 1][w])
            else:
                matrice[i][w] = matrice[i - 1][w]

    w = budget
    n = len(actions)
    actions_selection = []

    while w >= 0 and n >= 0:
        e = actions[n - 1]
        if matrice[n][int(w)] == matrice[n - 1][int(w - e[1])] + e[2]:
            actions_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], actions_selection


result_algo_dyn = algo_dynamic(500, clean_rows_dyn)
print('result', result_algo_dyn)

total_cost = list(map(lambda x: x[1], result_algo_dyn[1]))
print("total_cost", total_cost)
total_cost_list = list(total_cost)
total_cost_deux = sum(total_cost_list)


def write_report(choice, array_item, total_invest, benefice_report):
    if path.exists(f'./results/{choice}.txt'):
        remove(f'./results/{choice}.txt')

    result_for_file = ""
    for action in array_item:
        result_for_file += f"{action[0]:<10}- price: {action[1]:>6.2f} € / profit: {action[2]:>6.2f} €\n"

    with open(f'./results/{choice}.txt', 'xt') as result_file:
        result_file.write(f"\nActions to select for best return : \n\n"
                          f"{result_for_file}"
                          f"\nTotal cost: {benefice_report:>6.2f} € \n"
                          f"Total return: {total_invest:>6.2f} €\n\n")


write_report('optimized', result_algo_dyn[1], result_algo_dyn[0], total_cost_deux)

time_fin = time() - time_debut
print("time_fin", time_fin)
