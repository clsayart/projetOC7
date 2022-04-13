from time import time
import csv
from os import path, remove

time_debut = time()

# with open("files/actions_with_benefits.csv", 'r') as file_2:
# with open("files/data1_test.csv", 'r') as file_2:

rows_2 = []
with open("files/actions_with_benefits.csv", 'r') as file_2:
    csv_reader_2 = csv.reader(file_2)
    header_2 = next(csv_reader_2)
    for row in csv_reader_2:
        rows_2.append(row)
print("header", header_2)
print("rows", rows_2)


clean_rows_bf = []
for row in rows_2:
    print('row', row)
    if float(row[1]) > 0 and float(row[2]) > 0:  # remove null or negative values
        clean_rows_bf.append((row[0], float(row[1]), float(row[2])))

print('clean rows', clean_rows_bf)


# print("rows", rows)

# rows_2 = []
# with open("files/actions_with_benefits.csv", 'r') as file:
#     csv_reader = csv.reader(file)
#     header = next(csv_reader)
#     for row in csv_reader:
#         rows_2.append(row)
# print("header", header)
# print("rows", rows)


def benefice(actions_array):
    benefice_un = []
    for i in actions_array:
        ben = (int(i[1]) * int(i[2])) / 100
        benefice_un.append([i[0], float(i[1]), round(ben, 2)])
    return benefice_un


# print("benefice(rows)", benefice(rows))

# Details = ['Action Name', 'Price', 'Benefit']
# rows_ben = benefice(rows)
# with open('files/actions_with_benefits.csv', 'w', newline="") as f:
#     write = csv.writer(f)
#     write.writerow(Details)
#     write.writerows(rows_ben)


def algo_force_brute(budget, actions, selected_actions=[]):
    if actions:
        val1, list_val1 = algo_force_brute(budget, actions[1:], selected_actions)
        val = actions[0]
        if val[1] <= budget:
            val2, list_val2 = algo_force_brute(budget - val[1], actions[1:], selected_actions + [val])
            if val1 < val2:
                return val2, list_val2

        return val1, list_val1
    else:
        return sum([i[2] for i in selected_actions]), selected_actions


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


# result_algo = algo_force_brute(500, rows_ben)
# print("là")
result_algo_2 = algo_force_brute(500, clean_rows_bf)
print('result', result_algo_2)


total_cost_2 = list(map(lambda x: x[1], result_algo_2[1]))
total_cost_list_2 = list(total_cost_2)
total_cost_deux_2 = sum(total_cost_list_2)
print("je suis là")

write_report('bruteforce', result_algo_2[1], result_algo_2[0], total_cost_deux_2)

time_fin = time() - time_debut
print(time_fin)


