from utils import timer


def sum_of_multiplies(n, d):
    p = n // d
    s = p * (p + 1) // 2
    return s * d


@timer
def euler_1():
    n = 1000 - 1
    return (
        sum_of_multiplies(n, d=3)
        + sum_of_multiplies(n, d=5)
        - sum_of_multiplies(n, d=15)
    )


if __name__ == "__main__":
    print(euler_1())
