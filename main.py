from problems_11_20 import process_problems_11_20
from problems_1_10 import process_problems_1_10

def main():
    # process_problems_1_10()
    # process_problems_11_20()

    N = 220
    for x in range(1, N + 1):
        if (N % x == 0):
            print(x)

    # process_problem(problem_11, 4)
    # process_problem(problem_12, 500)
    # process_problem(problem_13, 10)
    # process_problem(problem_14, 1000000)
    # process_problem(problem_15, 20)
    # process_problem(problem_16, 1000)
    # process_problem(problem_17, 1000)
    # process_problem(problem_18, "")
    # process_problem(problem_19,"")
    # process_problem(problem_20, 100)


if __name__ == '__main__':
    main()
