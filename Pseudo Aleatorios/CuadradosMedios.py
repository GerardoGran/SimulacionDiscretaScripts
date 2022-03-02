import math


def get_digits(n: int):
    return len(str(n))


def extract_mid(n: int, d: int):
    print(f"x_Sq:{n}")
    size = get_digits(n)
    remove = size - d
    if size % 2:
        return int(str(n)[math.ceil(
            remove/2) + 1:math.ceil(remove/2) + d + 1])
    else:
        return int(f"0{str(n)}"[math.ceil(
            remove/2 + 1):math.ceil(remove/2 + 1) + d])


def cuadrados_medios(semilla: int, num_deseados: int):
    nums = []
    x = semilla
    for i in range(num_deseados):
        print(f"x{i}: {x}")
        d = get_digits(x)
        x_squared = x**2
        x = extract_mid(x_squared, d)
        nums.append(float(f"0.{x}"))
        print(f"r{i+1}: 0.{x}")

    print(nums)


cuadrados_medios(5735, 5)
