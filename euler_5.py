from utils import timer
from math import lcm


@timer
def euler_5():
    return lcm(*list(range(1, 21)))


if __name__ == "__main__":
    print(euler_5())
