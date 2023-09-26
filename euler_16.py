from utils import timer


@timer
def euler_16() -> int:
    number = 2**1000
    return sum(map(int, str(number)))


if __name__ == "__main__":
    print(euler_16())
