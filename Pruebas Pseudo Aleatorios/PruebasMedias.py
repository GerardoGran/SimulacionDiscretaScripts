# remember to use python 3.8 or higher
from ast import List
import math
from statistics import NormalDist


def getAvg(nums: list) -> float:
    return sum(nums) / len(nums)


def getLowerLimit(alpha: float, n: int) -> float:
    return 0.5 + (NormalDist().inv_cdf(alpha / 2) * (1 / (math.sqrt(12 * n))))


def getUpperLimit(alpha: float, n: int) -> float:
    return 0.5 - (NormalDist().inv_cdf(alpha / 2) * (1 / (math.sqrt(12 * n))))


def prueba_medias(nums: list) -> None:
    r = getAvg(nums)

    lower = getLowerLimit(0.05, len(nums))
    higher = getUpperLimit(0.05, len(nums))
    if r < higher and r > lower:
        print("Media: ACEPTADA")
        print(
            f"Dado que: r: {r}, limite inf: {lower} y limite sup: {higher}, No se rechaza H0\n"
        )
        return True
    else:
        print("Media: RECHAZADA")
        print(
            f"Dado que: r: {r}, limite inf: {lower} y limite sup: {higher}, Se rechaza H0\n"
        )

        return False
