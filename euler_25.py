from utils import timer
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(index: int) -> int:
    if index in {1, 2}:
        return 1
    return fibonacci(index - 1) + fibonacci(index - 2)


@timer
def euler_25() -> int:
    answer = 1
    while len(str(fibonacci(answer))) < 1000:
        answer += 1
    return answer


if __name__ == "__main__":
    print(euler_25())
