from utils import timer


@timer
def euler_6():
    n = 100
    sqr_sum = (n * (n + 1) // 2) ** 2
    sum_sqr = sum(x**2 for x in range(1, n + 1))
    return abs(sqr_sum - sum_sqr)


if __name__ == "__main__":
    print(euler_6())
