from utils import timer


@timer
def euler_10():
    n = 2000000
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    for k in range(int(len(primes) ** 0.5) + 1):
        if primes[k]:
            for m in range(2 * k, len(primes), k):
                primes[m] = False
    return sum(p for p in range(len(primes)) if primes[p])


if __name__ == "__main__":
    print(euler_10())
