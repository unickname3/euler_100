from utils import timer, get_primes_list


def count_divisors(number: int, primes_list: list[int]) -> int:
    result = 1
    for el in primes_list:
        power = 0
        while number % el == 0:
            power += 1
            number /= el
        result *= power + 1
        if number < el:
            break
    return result


@timer
def euler_12() -> int:
    primes = get_primes_list(quantity_of_primes=500)
    triangle = 1
    step = 2
    while count_divisors(triangle, primes) <= 500:
        triangle += step
        step += 1
    return triangle


if __name__ == "__main__":
    print(euler_12())
