from utils import timer


@timer
def euler_65():
    a = [2, 1, 2]
    k = 2
    for i in range(1, 100):
        if i % 3 == 0:
            a.append(2 * k)
            k += 1
        else:
            a.append(1)

    p = [1, a[0]]
    for i in range(1, 100):
        p.append(p[i] * a[i] + p[i - 1])
    s = str(p[100])

    return sum(map(int, s))


if __name__ == "__main__":
    print(euler_65())
