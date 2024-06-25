from problems_11_20 import process_problems_11_20
from problems_1_10 import process_problems_1_10
from util import process_problem


def sum_of_divisors(n):
    z = 0
    for i in range(1, n):
        if n % i == 0:
            z = z + i
    return z

def problem_21(args):
    # 31626
    total_sum = 0
    # start at 200 since we know 1st one is greater than 200
    a = 200

    while True:
        a = a + 2
        done = False
        loc_sum = sum_of_divisors(a)
        for i in range(a, args[1], 2):
            if done:
                break
            if a >= (args[1] - 2):
                return total_sum
            if (loc_sum == i) and (sum_of_divisors(i) == a) and (a != i):
                # txt = f"({a},{i})"
                # print(txt)
                total_sum = total_sum + i + a
                a = i
                done = True


def main():
    # process_problems_1_10()
    # process_problems_11_20()

    process_problem(problem_21, 10000)

    # print(sum_of_divisors(220))
    # print(sum_of_divisors(284))
    # if (sum_of_divisors(220) == 284) and (sum_of_divisors(284) == 220):
    #     print('220, 284 are amicable numbers')


if __name__ == '__main__':
    main()
