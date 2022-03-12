str_nums = "0.347 0.832 0.966 0.472 0.797 0.101 0.696 0.966 0.404 0.603 0.993 0.371 0.729 0.067 0.189 0.977 0.843 0.562 0.549 0.992 0.674 0.628 0.055 0.494 0.494 0.235 0.178 0.775 0.797 0.252 0.426 0.054 0.022 0.742 0.674 0.898 0.641 0.674 0.821 0.19 0.46 0.224 0.99 0.786 0.393 0.461 0.011 0.977 0.246 0.881 0.189 0.753 0.73 0.797 0.292 0.876 0.707 0.562 0.562 0.821 0.112 0.191 0.584 0.347 0.426 0.057 0.819 0.303 0.404 0.64 0.37 0.314 0.731 0.742 0.213 0.472 0.641 0.944 0.28 0.663 0.909 0.764 0.999 0.303 0.718 0.933 0.056 0.415 0.819 0.444 0.178 0.516 0.437 0.393 0.268 0.123 0.945 0.527 0.459 0.652".split(
    " ")
nums = map((lambda x: float(x)), str_nums)


def get_range(n):
    if n > 0.5:
        if n > 0.7:
            if n > 0.9:
                return 9
            elif n > 0.8:
                return 8
            else:
                return 7
        elif n > 0.6:
            return 6
        else:
            return 5
    elif n > 0.3:
        if n > 0.4:
            return 4
        else:
            return 3
    elif n > 0.1:
        if n > 0.2:
            return 2
        else:
            return 1
    else:
        return 0


def prueba_uniformidad(nums):
    rangos = [[], [], [], [], [], [], [], [], [], []]
    for n in nums:
        rangos[get_range(n)].append(n)

    frecuencias = map(lambda arr: len(arr), rangos)

    for i, n in enumerate(frecuencias):
        print(f"{i/10} - {(i + 1)/10}: {n} -> Chisq = {(10-n)**2/10}")


prueba_uniformidad(nums)
