from hashlib import new


n = int(input("Enter size of list: "))
arr = []
for i in range(0, n):
    arr.append(int(input(f"Enter x{i}: ")))

m = int(input("Enter m: "))

amount = int(input("Enter amount of rndm numbers: "))


def getNewX(XiMinusOne, XiMinusN, m):
    return (XiMinusOne + XiMinusN) % m


def r(x, m):
    return x / (m - 1)


results = []

for i in range(n, amount + n):
    newX = getNewX(arr[i - 1], arr[i - n], m)
    arr.append(newX)
    results.append("%.5f" % r(newX, m))

print(results)
