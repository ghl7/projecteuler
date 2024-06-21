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
    total_sum = 0
    a = 100
    b = int(1.2 * a)

    while True:
        for i in range(a+2, b, 2):
            if b > args[1]:
                return total_sum
            if (sum_of_divisors(a) == i) and (sum_of_divisors(a) == i):
                print(a)
                print(i)
                total_sum = total_sum + i + a
                i = b
                a = a + 2
                b = int(1.2 * a)


def main():
    # process_problems_1_10()
    # process_problems_11_20()

    process_problem(problem_21, 10000)

    print(sum_of_divisors(220))
    print(sum_of_divisors(284))
    if (sum_of_divisors(220) == 284) and (sum_of_divisors(284) == 220):
        print('220, 284 are amicable numbers')


if __name__ == '__main__':
    main()
