def r(xi: int, m: int):
    return xi / (m - 1)


def getX(x: int, a: int, c: int, m: int):
    return (x * a + c) % m


def algoritmo_lineal(seed: int, a: int, c: int, m: int, n: int):
    nums = []
    x = getX(seed, a, c, m)

    for i in range(n):
        nums.append(f"{r(x, m):.4f}")
        x = getX(x, a, c, m)

    print(f"xi+1 = ({a}xi + {c})mod({m}): {nums}")


seed = int(input("Semilla (x0): "))
a = int(input("Constante multiplicativa (a): "))
c = int(input("Constante Aditiva (c): "))
m = int(input("m: "))
n = int(input("Cuantos Numeros: "))

algoritmo_lineal(seed, a, c, m, n)
