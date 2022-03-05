def get_digits(n: int):
    return len(str(n))


def extract_mid(n: int, d: int):
    size = get_digits(n)
    remove = size - d   # Digits to remove
    if size % 2 == 1:
        str_num = f"0{n}"
    else:
        str_num = str(n)

    return str(str_num)[remove // 2: remove // 2 + d]


def productos_medios(semilla_1: int, semilla_2: int, num_deseados: int):
    nums = []
    factores = (semilla_1, semilla_2)
    for i in range(num_deseados):
        d = get_digits(factores[0])
        producto = factores[0] * factores[1]
        r = extract_mid(producto, d)
        nums.append(float(f"0.{r}"))
        factores = (factores[1], int(r))

    print(
        f"Xo = {semilla_1}, x1 = {semilla_2}, D = {get_digits(semilla_1)}: {nums}")


seed1 = int(input("Ingresa la semilla1: "))
seed2 = int(input("Ingresa la semilla2: "))

n = int(input("Ingresa la cantidad de numeros: "))

productos_medios(seed1, seed2, n)