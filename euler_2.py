from utils import timer


def fibonacci():
    prev_prev = 0
    prev = 1
    while True:
        next = prev + prev_prev
        prev_prev, prev = prev, next
        yield next


@timer
def euler_2():
    n = 4000000
    fib = fibonacci()
    next_number = next(fib)
    result = 0
    while next_number <= n:
        if next_number % 2 == 0:
            result += next_number
        next_number = next(fib)
    return result


if __name__ == "__main__":
    print(euler_2())
