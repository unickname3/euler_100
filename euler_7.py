from utils import timer, get_primes_list


@timer
def euler_7():
    n = 10001
    return get_primes_list(quantity_of_primes=n)[-1]


if __name__ == "__main__":
    print(euler_7())
