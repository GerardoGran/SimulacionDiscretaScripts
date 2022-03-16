# remember to use python 3.8 or higher  
from ast import List
import math
from statistics import NormalDist

def getAvg(input: list) -> float:
    sum = 0
    for number in input:
        sum += number
    return sum / len(input)

def getLowerLimit(alpha: float, n: int) -> float:
    return 0.5 + (NormalDist().inv_cdf(alpha / 2) * (1 / (math.sqrt(12 * n))))

def getUpperLimit(alpha: float, n: int) -> float:
    return 0.5 - (NormalDist().inv_cdf(alpha / 2) * (1 / (math.sqrt(12 * n))))

def pruebaMedias(input: list) -> None:
    r = getAvg(input_list)

    lower = getLowerLimit(0.05, len(input_list))
    higher = getUpperLimit(0.05, len(input_list))
    if r < higher and r > lower:
        print(f"Dado que: r: {r}, limite inf: {lower} y limite sup: {higher}, No se rechaza H0")
    else:
        print(f"Dado que: r: {r}, limite inf: {lower} y limite sup: {higher}, Se rechaza H0")


# problem input here
input_list = []

pruebaMedias(input_list)