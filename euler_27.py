import math


# TODO: Need to refactor
def F(a, b, n):
    return n**2 + a * n + b


def isPrime(q):
    if (q / 2).is_integer():
        return False
    i = 3
    print(".", end="")
    while i < math.sqrt(q) + 1:
        k = q / i
        if k.is_integer():
            return False
        i += 2
    return True


def listPrime(M):
    PrMat = [True] * M
    PrMat[0] = False
    PrMat[1] = False
    i = 2
    while i < M:
        if PrMat[i]:
            k = 2 * i
            while k < M:
                PrMat[k] = False
                k += i
        i += 1
    Pr = []
    for i in range(M):
        if PrMat[i]:
            Pr.append(i)
    return Pr


dep = 10000
Prime = listPrime(dep)
nMax = 0
for b in Prime:
    if b < 1001:
        for a in range(-1000, 1000):
            n = 0
            num = F(a, b, n)
            while (num > 0) and (num in Prime):
                n += 1
                num = F(a, b, n)
            if n > nMax:
                print(n, a, b, a * b)
                nMax = n
