from utils import timer


@timer
def euler_3():
    n = 600851475143
    k = 2
    result = 1
    while k <= n:
        while n % k == 0:
            n //= k
            result = max(result, k)
        k += 1
    return result


if __name__ == "__main__":
    print(euler_3())
