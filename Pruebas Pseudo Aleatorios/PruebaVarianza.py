from scipy.stats import chi2

nums = [
    0.0449,
    0.1733,
    0.5746,
    0.049,
    0.8406,
    0.849,
    0.92,
    0.2564,
    0.6015,
    0.6694,
    0.3972,
    0.7025,
    0.1055,
    0.1247,
    0.1977,
    0.0125,
    0.63,
    0.2531,
    0.8297,
    0.6483,
    0.6972,
    0.9582,
    0.9085,
    0.8524,
    0.5514,
    0.0316,
    0.3587,
    0.7041,
    0.5915,
    0.2523,
    0.2545,
    0.3044,
    0.0207,
    0.1067,
    0.3857,
    0.1746,
    0.3362,
    0.1589,
    0.3727,
    0.4145,
]


def variance(arr):
    mean = sum(arr) / len(arr)
    total = 0
    for n in arr:
        total += (n - mean) ** 2

    return total / (len(arr) - 1)


def lim_inf(alpha: float, n: int):
    freedom = n - 1
    chi = chi2.ppf(alpha / 2, freedom)
    return chi / (12 * freedom)


def lim_sup(alpha: float, n: int):
    freedom = n - 1
    chi = chi2.ppf(1 - alpha / 2, freedom)
    return chi / (12 * freedom)


def prueba_varianza(nums, alpha):
    var = variance(nums)
    inf = lim_inf(alpha, len(nums))
    sup = lim_sup(alpha, len(nums))
    print(f"V: {var}\nLi: {inf}, Ls: {sup}")

    if inf < var and var < sup:
        print("Se acepta")
    else:
        print("Se rechaza")


prueba_varianza(nums, 0.05)
