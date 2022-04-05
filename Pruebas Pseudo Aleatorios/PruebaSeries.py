from functools import total_ordering
from scipy.stats import chi2
from tabulate import tabulate


def encontrar_casilla(x: int, y: int) -> int:
    """Regresa numero correspondiente de la casilla a la que pertenecen los pares de numeros"""
    DIV_2 = 0.66
    DIV_1 = 0.33
    if y > DIV_2:
        if x > DIV_2:
            return 8
        elif x > DIV_1:
            return 7
        else:
            return 6
    elif y > DIV_1:
        if x > DIV_2:
            return 5
        elif x > DIV_1:
            return 4
        else:
            return 3
    else:
        if x > DIV_2:
            return 2
        elif x > DIV_1:
            return 1
        else:
            return 0


def prueba_series(nums: list, alpha: float = 0.05) -> bool:
    print("Prueba Series:")
    casillas = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(len(nums) - 1):
        posicion = encontrar_casilla(nums[i], nums[i + 1])
        casillas[posicion] += 1

    Ei = (len(nums) - 1) / 9

    data = []
    chisq_sum = 0
    headers = ["casilla", "Oi", "Ei", "Chisq"]
    for i in range(len(casillas)):
        chisq = ((Ei - casillas[i]) ** 2) / Ei
        chisq_sum += chisq
        data.append([i + 1, casillas[i], Ei, chisq])

    print(tabulate(data, headers))
    print(f"La suma de chisq es {chisq_sum:.3f}")

    if chi2.ppf(1 - alpha, 8) > chisq_sum:
        print(f"{chi2.ppf(1-alpha, 8):.3f} > {chisq_sum:.3f}, se acepta")
        return True
    else:
        print(f"{chi2.ppf(1-alpha, 8):.3f} < {chisq_sum:.3f}, se rechaza")
        return False
