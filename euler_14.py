from utils import timer
from functools import lru_cache


@lru_cache(maxsize=None)
def count_step(num: int) -> int:
    if num == 1:
        return 0
    if num % 2 == 0:
        return count_step(num // 2) + 1
    else:
        return count_step((3 * num + 1) // 2) + 2


@timer
def euler_14() -> int:
    longest_path = 0
    number_with_longest_path = 0
    for n in range(500000, 1000000):
        path_len = count_step(n)
        if path_len > longest_path:
            number_with_longest_path = n
            longest_path = path_len
        # print(f"For {n} path {path_len}")
    return number_with_longest_path


if __name__ == "__main__":
    print(euler_14())
