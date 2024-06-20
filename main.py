from problems_11_20 import process_problems_11_20
from problems_1_10 import process_problems_1_10

def sum_of_divisors(n):
    z = 0
    for i in range(1, n):
        if n % i == 0:
            z = z + i
    return z

def main():
    # process_problems_1_10()
    # process_problems_11_20()

    print(sum_of_divisors(220))
    print(sum_of_divisors(284))
    if (sum_of_divisors(220) == 284) and (sum_of_divisors(284) == 220):
        print('220, 284 are amicable numbers')


if __name__ == '__main__':
    main()
