from functools import reduce
from math import factorial, pow, exp


def poisson(x: int, lam: int):
    return (exp(-lam)*pow(lam, x))/factorial(x)


def poisson_exacto(x: int, lam: int):
    sum_x = reduce((lambda i, j: poisson(i, lam) +
                   poisson(j, lam)), range(1, x+1))
    print(sum_x)


poisson_exacto(6, 4)
