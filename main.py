from bruteforce import run_algo_force_brute
from optimized import run_algo_dynamic

print("\nalgoInvest program\n")

exit_algo_app = False

while not exit_algo_app:
    print(" Choose an algorithm: \n\n"
          "1- Bruteforce (just for 20 actions)\n"
          "2- Optimized \n")
    choice_algo = 0
    choice_file = 0
    choice_file_test = False

    while not choice_file_test:
        try:
            choice_algo = int(input("Your choice : "))
            if choice_algo == 1 or choice_algo == 2:
                choice_file_test = True
        except ValueError:
            print("Your choice must be 1, 2")

    if choice_algo == 1:
        run_algo_force_brute('files/dataset20actions.csv')

    elif choice_algo == 2:
        print("Which file do you want to test ?\n"
              "1- Dataset 20 actions\n"
              "2- Dataset 1\n"
              "3- Dataset 2\n")
        choice_file_test = False
        while not choice_file_test:
            try:
                choice_file = int(input("Your choice : "))
                if choice_file == 1 or choice_file == 2 or choice_file == 3 or choice_file == 4:
                    choice_file_test = True
            except ValueError:
                print("Your choice must be 1, 2, 3 or 4")

        if choice_file == 1:
            csv_file = 'files/dataset20actions.csv'
            run_algo_dynamic(csv_file)
        if choice_file == 2:
            csv_file = 'files/dataset1_Python+P7.csv'
            run_algo_dynamic(csv_file)
        if choice_file == 3:
            csv_file = 'files/dataset2_Python+P7.csv'
            run_algo_dynamic(csv_file)

    choice_end = input("End algoInvest program ? (Y/n) : ")

    if choice_end.upper() == 'Y':
        exit_algo_app = True
