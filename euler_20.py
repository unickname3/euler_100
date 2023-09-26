from utils import timer


def factorial(number: int) -> int:
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)


@timer
def euler_20() -> int:
    number = factorial(100)
    return sum(map(int, str(number)))


if __name__ == "__main__":
    print(euler_20())
