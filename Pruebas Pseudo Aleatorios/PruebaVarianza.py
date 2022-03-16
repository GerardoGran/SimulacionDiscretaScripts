from scipy.stats import chi2


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
