from utils import timer


@timer
def euler_7():
    n = 10001
    primes = [2]
    k = 3
    while len(primes) < n:
        edge = k**0.5
        for d in primes:
            if d > edge:
                primes.append(k)
                break
            if k % d == 0:
                break
        else:
            primes.append(k)
        k += 2
    return primes[-1]


if __name__ == "__main__":
    print(euler_7())
