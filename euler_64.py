import math

from utils import timer


def get_full(f):
    r = [f[2], -f[3], 0, (f[2] - f[3] ** 2) // f[1]]
    while math.sqrt(r[0]) + r[1] > r[3]:
        r[1] -= r[3]
    return r


def rev(f2):
    r2 = [f2[2], f2[3], f2[0], f2[1]]
    return r2


def period_length(N):
    a = int(math.sqrt(N))
    x = [[N, -a, 0, 1]]
    while True:
        next_x = get_full(rev(x[-1]))
        if next_x in x:
            return len(x) - x.index(next_x)
        x.append(next_x)


@timer
def euler_64():
    result = 0
    for k in range(10001):
        if not (math.sqrt(k)).is_integer():
            result += period_length(k) % 2
    return result


if __name__ == "__main__":
    print(euler_64())
