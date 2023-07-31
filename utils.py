from functools import wraps
import time
from math import log


def timer(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(f"Function {function.__qualname__} took {time.time() - start_time:.2f}s")
        return result

    return wrapped


def how_many_numbers(quantity_of_primes: int) -> int:
    """
    The function calculates what N should be so that there are at least quantity_of_primes primes in the range from 1 to N.
    """
    answer = 2
    while quantity_of_primes >= answer / log(answer):
        answer *= 2
    return answer


def get_primes_list(less_than: int = 0, quantity_of_primes: int = 0) -> list[int]:
    """
    Fumction return list of primes numbers with quantity_of_primes primes numbers less than less_than
    """
    if less_than == 0:
        less_than = how_many_numbers(quantity_of_primes=quantity_of_primes)

    is_primes = [True] * (less_than)
    is_primes[0] = False
    is_primes[1] = False

    for k in range(int(len(is_primes) ** 0.5) + 1):
        if is_primes[k]:
            for m in range(2 * k, len(is_primes), k):
                is_primes[m] = False

    primes = [p for p in range(len(is_primes)) if is_primes[p]]

    if quantity_of_primes != 0:
        return primes[:quantity_of_primes]

    return primes
