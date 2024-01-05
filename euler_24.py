import itertools

from utils import timer


@timer
def euler_24():
    s = "0123456789"
    digit_permutations = list(itertools.permutations(s))
    return "".join(digit_permutations[999999])


if __name__ == "__main__":
    print(euler_24())
