from utils import timer
from utils import get_primes_list


@timer
def euler_10():
    n = 2000000
    return sum(get_primes_list(less_than=n))


if __name__ == "__main__":
    print(euler_10())
