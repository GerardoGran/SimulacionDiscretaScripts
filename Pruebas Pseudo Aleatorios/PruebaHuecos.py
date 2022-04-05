from scipy.stats import chi2
from tabulate import tabulate


def prueba_huecos(nums: list, rango: tuple, alpha: float = 0.05) -> bool:
    huecos = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    s = []  # Indicadores si estan en el rango
    for n in nums:
        s.append(n >= rango[0] and n <= rango[1])

    started = False
    count = 0
    for n in s:
        if started:
            if n:
                if count >= 5:
                    huecos[5] += 1
                else:
                    huecos[count] += 1
                count = 0
            else:
                count += 1
        elif n:
            started = True

    data = []
    headers = ["Tamano hueco", "Oi", "Ei", "Chisq"]

    h = sum(huecos.values())
    chisq_sum = 0
    for i in huecos:
        Oi = huecos[i]
        Ei = h * rango[0] * rango[1] ** i
        chisq = ((Ei - Oi) ** 2) / Ei
        chisq_sum += chisq
        if i != 5:
            data.append([i, Oi, Ei, chisq])
        else:
            data.append(["5+", Oi, Ei, chisq])

    print(tabulate(data, headers))

    chisq_compare = chi2.ppf(1 - alpha, 5)
    if chisq_compare > chisq_sum:
        print(f"{chisq_compare:.3f} > nuestro {chisq_sum:.3f}, se acepta")
        return True
    else:
        print(f"nuestro {chisq_sum:.3f} > {chisq_compare:.3f}, se rechaza")
        return False
