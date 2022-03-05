def get_digits(n: int):
    return len(str(n))


def extract_mid(n: int, d: int):
    size = get_digits(n)
    remove = size - d   # Digits to remove
    if size % 2 == 1:
        str_num = f"0{n}"
        remove += 1
    else:
        str_num = str(n)

    return str(str_num)[remove // 2: remove // 2 + d]


def productos_medios(semilla_1: int, a: int, num_deseados: int):
    nums = []
    r = semilla_1
    d = get_digits(r)
    for i in range(num_deseados):
        producto = int(r) * a
        r = extract_mid(producto, d)
        nums.append(float(f"0.{r}"))

    print(
        f"Xo = {semilla_1}, a = {a}, D = {get_digits(semilla_1)}: {nums}")


seed1 = int(input("Ingresa la semilla1: "))
seed2 = int(input("Ingresa la constante: "))

n = int(input("Ingresa la cantidad de numeros: "))

productos_medios(seed1, seed2, n)