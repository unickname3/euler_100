import math

from utils import timer


def get_full(f):
    r = [f[2], -f[3], 0, (f[2] - f[3] ** 2) // f[1]]
    full = 0
    while math.sqrt(r[0]) + r[1] > r[3]:
        r[1] -= r[3]
        full += 1
    return [full, r]


def rev(f2):
    r2 = [f2[2], f2[3], f2[0], f2[1]]
    return r2


def solve_Pelle(D):
    a = [int(math.sqrt(D))]
    x = [[D, -a[0], 0, 1]]
    j = 1
    p = [1, a[0]]
    q = [0, 1]
    while True:
        next_a, next_x = get_full(rev(x[j - 1]))
        a.append(next_a)
        x.append(next_x)
        p.append(a[j] * p[j] + p[j - 1])
        q.append(a[j] * q[j] + q[j - 1])
        if p[j] ** 2 - D * q[j] ** 2 == 1:
            return p[j]
        j += 1


@timer
def euler_66():
    target_D = 0
    largest_x = 0
    for D in range(1001):
        if not (math.sqrt(D)).is_integer():
            x = solve_Pelle(D)
            if x > largest_x:
                largest_x = x
                target_D = D
    return target_D


if __name__ == "__main__":
    print(euler_66())
