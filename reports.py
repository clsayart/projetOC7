from os import path, remove
import csv


def write_report(choice, array_item, total_invest, benefice_report):
    if path.exists(f'./results/{choice}.txt'):
        remove(f'./results/{choice}.txt')

    result_for_file = ""
    for action in array_item:
        result_for_file += f"{action[0]:<10}- price: {action[1]:>6.2f} Euros / profit: {action[2]:>6.2f} Euros\n"

    with open(f'./results/{choice}.txt', 'xt') as result_file:
        result_file.write(f"\nActions to select for best return : \n\n"
                          f"{result_for_file}"
                          f"\nTotal cost: {total_invest:>6.2f} Euros \n"
                          f"Total return: {benefice_report:>6.2f} Euros\n\n")


def file_to_rows(filename):
    rows_array = []
    with open(filename, 'r') as file_in_def:
        csv_reader_in_def = csv.reader(file_in_def)
        header_in_def = next(csv_reader_in_def)
        for one_row in csv_reader_in_def:
            rows_array.append(one_row)
    return rows_array
