import math
import sys
import sympy
from sympy import factorint

from util import process_problem

def problem_1(args):
    z = 0
    for i in range(3, args[1]):
        if i % 3 == 0 or i % 5 == 0:
            z = z + i
            # lst.append(i)
    return z

def problem_2(args):
    z = 0
    current = 2
    previous = 1
    while current < args[1]:
        if current % 2 == 0:
            z = z + current
        x = current
        current = current + previous
        previous = x
    return z

def problem_3(args):
    a = factorint(args[1])
    key, value = list(a.items())[len(a)-1]
    return key

def problem_4(args):
    a = int(math.floor(math.sqrt(args[1]))-1)
    aa = int(math.floor(math.sqrt(a)))
    c = 0
    for i in range(a, aa, -1):
        for j in range(a, aa, -1):
            x = i*j
            if x == int(str(x)[::-1]):
                if c < x:
                    c = x
    return c

def problem_5(args):
    c = list(sympy.sieve.primerange(1, args[1]))
    y = 1
    for i in range(0, len(c)):
        n = 0
        x = c[i]
        while x < args[1]:
            x = x * c[i]
            n = n + 1
        y = y * c[i]**n
    return y


def problem_6(args):
    x = 0
    y = 0
    for i in range(1, args[1]+1):
        x = x + i
        y = y + i**2
    return x**2 - y

def problem_7(args):
    return sympy.prime(args[1])

def problem_8(args):
    arr = \
        '73167176531330624919225119674426574742355349194934' + \
        '96983520312774506326239578318016984801869478851843' + \
        '85861560789112949495459501737958331952853208805511' + \
        '12540698747158523863050715693290963295227443043557' + \
        '66896648950445244523161731856403098711121722383113' + \
        '62229893423380308135336276614282806444486645238749' + \
        '30358907296290491560440772390713810515859307960866' + \
        '70172427121883998797908792274921901699720888093776' + \
        '65727333001053367881220235421809751254540594752243' + \
        '52584907711670556013604839586446706324415722155397' + \
        '53697817977846174064955149290862569321978468622482' + \
        '83972241375657056057490261407972968652414535100474' + \
        '82166370484403199890008895243450658541227588666881' + \
        '16427171479924442928230863465674813919123162824586' + \
        '17866458359124566529476545682848912883142607690042' + \
        '24219022671055626321111109370544217506941658960408' + \
        '07198403850962455444362981230987879927244284909188' + \
        '84580156166097919133875499200524063689912560717606' + \
        '05886116467109405077541002256983155200055935729725' + \
        '71636269561882670428252483600823257530420752963450'
    # convert to int array
    c = []
    for i in range(0, len(arr)):
        c.append(int(arr[i]))
    # sweep array from 0 to arr size - window width args[1]
    window_width = args[1]
    max_prod = 0
    for i in range(0, len(arr)-window_width):
        # get next prods of windows width and check for max
        prods = 1
        for j in range(i, i+window_width):
            prods = prods * c[j]
        if max_prod < prods:
            max_prod = prods
    return max_prod

def pythagorean_triple(m, n):
    if n >= m:
        print('pythagorean_triple error, m <= n')
        sys.exit(-1)
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return a, b, c

def problem_9(args):
    for a in range(2, 1000):
        for b in range(2, a):
            x = pythagorean_triple(a, b)
            y = x[0] + x[1] + x[2]
            if y == args[1]:
                # print("<{0}, {1}, {2}>".format(x[0], x[1], x[2]))
                return x[0] * x[1] * x[2]

def problem_10(args):
    return sum(list(sympy.sieve.primerange(1, args[1])))

def process_problems_1_10():
    process_problem(problem_1, 1000)
    process_problem(problem_2, 4000000)
    process_problem(problem_3, 600851475143)
    process_problem(problem_4, 1000000)
    process_problem(problem_5, 20)
    process_problem(problem_6, 100)
    process_problem(problem_7, 10001)
    process_problem(problem_8, 13)
    process_problem(problem_9, 1000)
    process_problem(problem_10, 2000000)
