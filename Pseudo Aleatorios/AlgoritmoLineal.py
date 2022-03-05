seed = int(input("Enter the seed: "))
a = int(input("Enter a: "))
c = int(input("Enter c: "))
m = int(input("Enter m: "))
n = int(input("Enter amount: "))

counter = 0

def r(xi, m):
    return xi / (m - 1)

def getX(x, a, c, m):
    return (x * a + c) % m

newX = seed
results = []
while counter < n:
    newX = getX(newX, a, c, m)
    results.append("%.4f" % r(newX, m))
    counter += 1

print(results)