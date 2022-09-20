from time import time
from reports import file_to_rows, write_report


def benefice(actions_array):
    benefice_un = []
    for i in actions_array:
        ben = (float(i[1]) * float(i[2])) / 100
        benefice_un.append([i[0], float(i[1]), ben])
    return benefice_un


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


def run_algo_force_brute(csv_file):
    time_debut = time()
    array_rows = file_to_rows(csv_file)
    benefice_rows = benefice(array_rows)
    result_algo_2 = algo_force_brute(500, benefice_rows)
    total_cost_2 = list(map(lambda x: x[1], result_algo_2[1]))
    total_cost_list_2 = list(total_cost_2)
    total_cost_deux_2 = sum(total_cost_list_2)
    # write_report('bruteforce', result_algo_2[1], total_cost_deux_2, result_algo_2[0])
    time_fin = time() - time_debut
    print(f'Execution time : {time_fin} seconds\n'
          f'Return : {result_algo_2[0]} Euros\n'
          f'Cost : {total_cost_deux_2} Euros\n'
          )

# if __name__ == "__main__":
#     print("main")
#     run_algo_force_brute('files/actions_with_benefits.csv')
