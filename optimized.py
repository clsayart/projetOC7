from time import time
from reports import file_to_rows, write_report


def clean_values(array_rows):
    clean_rows_dyn = []
    for row in array_rows:
        if float(row[1]) > 0 and float(row[2]) > 0:  # remove null or negative values
            clean_rows_dyn.append((row[0], float(row[1]), float(row[2])))
    return clean_rows_dyn


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


def run_algo_dynamic(csv_file):
    time_debut = time()
    array_rows = file_to_rows(csv_file)
    clean_rows_dyn = clean_values(array_rows)
    result_algo_dyn = algo_dynamic(500, clean_rows_dyn)
    total_cost = list(map(lambda x: x[1], result_algo_dyn[1]))
    total_cost_list = list(total_cost)
    total_cost_deux = sum(total_cost_list)
    write_report('optimized', result_algo_dyn[1], result_algo_dyn[0], total_cost_deux)
    time_fin = time() - time_debut
    print(f'Execution time : {time_fin} seconds\n')


# if __name__ == "__main__":
#     print("dynamic")
#     run_algo_dynamic('files/dataset1_Python+P7.csv')
