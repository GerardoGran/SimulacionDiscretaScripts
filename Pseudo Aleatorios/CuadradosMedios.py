def get_digits(n: int):
    return len(str(n))


def extract_mid(n: int, d: int):
    size = get_digits(n)
    remove = size - d  # Digits to remove
    if size % 2 == 1:
        str_num = f"0{n}"
        remove += 1
    else:
        str_num = str(n)

    return str(str_num)[remove // 2 : remove // 2 + d]


def cuadrados_medios(semilla: int, num_deseados: int):
    nums = []
    x = semilla
    period = 0
    for i in range(num_deseados):
        d = get_digits(x)
        x_squared = int(x) ** 2
        x = extract_mid(x_squared, d)
        r = float(f"0.{x}")
        if r not in nums:
            period += 1
        nums.append(r)

    print(f"Xo = {semilla}, D = {get_digits(semilla)}:\n {nums}\n periodo: {period}")


seed = int(input("Ingresa la semilla: "))

n = int(input("Ingresa numeros deseados: "))

cuadrados_medios(seed, n)
