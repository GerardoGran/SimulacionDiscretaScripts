seed = int(input("Enter seed: "))
k = int(input("Enter k: "))
g = int(input("Enter g: "))
n = int(input("Enter amount: "))

def getM(g):
    return 2 ** g

def getA(k):
    return 5 + 8*k

def getNextX(x, a, m):
    return (a * x) % m

def r(x, m):
    return x / (m - 1)

a = getA(k)
m = getM(g)

count = 0
Xi = seed
while count < n:
    #do stuff
    Xi = getNextX(Xi, a, m)
    print(r(Xi, m))
    count += 1