from problems_11_20 import process_problems_11_20
from problems_1_10 import process_problems_1_10
from util import process_problem
import re


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
        a = a + 1
        done = False
        loc_sum = sum_of_divisors(a)
        for i in range(a, args[1], 1):
            if done:
                break
            if a >= (args[1] - 1):
                return total_sum
            if (loc_sum == i) and (sum_of_divisors(i) == a) and (a != i):
                # print(f"({a},{i})")
                total_sum = total_sum + i + a
                a = i
                done = True

def problem_22(args):
    # 871198282
    f = open(args[1])
    t = f.read()
    f.close()
    t = re.sub('"', '', t)
    x = re.split(',', t)
    x.sort()
    total_sum = 0
    for i in range(len(x)):
        y = list(x[i])
        s = 0
        for j in range(len(y)):
            s = s + (ord(y[j]) - ord('A') + 1)
        total_sum = total_sum + s * (i+1)
        # print(f"{i} {x[i]} {y} {s} {total_sum}")
    return total_sum

def problem_23(args):
    return 0

def main():
    # process_problems_1_10()
    # process_problems_11_20()

    # process_problem(problem_21, 10000)
    # process_problem(problem_22, "0022_names.txt")
    process_problem(problem_23, 28123)

    x = sum_of_divisors(28)
    print(x)

if __name__ == '__main__':
    main()
