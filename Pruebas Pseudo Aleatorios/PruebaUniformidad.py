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


def prueba_uniformidad(nums, alpha):
    rangos = [[], [], [], [], [], [], [], [], [], []]
    for n in nums:
        rangos[get_range(n)].append(n)

    frecuencias = map(lambda arr: len(arr), rangos)

    chisq = 0

    for i, n in enumerate(frecuencias):
        chisq += (10 - n) ** 2 / 10

    if chisq < 16.919:
        print("Uniformidad: ACEPTADA")
    else:
        print("Uniformidad: RECHAZADA")


prueba_uniformidad(nums, 0.05)
