from math import factorial, pow


def combinaciones(n, x):
    return factorial(n)/(factorial(x)*factorial(n-x))


def binom(x, n, p):
    q = 1-p
    return combinaciones(n, x)*pow(p, x)*pow(q, n-x)
