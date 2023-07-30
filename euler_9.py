from utils import timer


def is_triplet(a, b, c):
    a, b, c = sorted((a, b, c))
    return a**2 + b**2 == c**2


@timer
def euler_9():
    for c in range(1000, 333, -1):
        for b in range(1000 - c - 1, (1000 - c) // 2, -1):
            a = 1000 - c - b
            if is_triplet(a, b, c):
                return a * b * c


if __name__ == "__main__":
    print(euler_9())
