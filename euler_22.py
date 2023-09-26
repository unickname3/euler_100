from utils import timer

NAMES_FILENAME = "0022_names.txt"


def score_count(name: str) -> int:
    return sum(ord(c) - ord("A") + 1 for c in name.upper())


@timer
def euler_22() -> int:
    with open(NAMES_FILENAME, "r") as f:
        names = f.read()
    names = names.replace('"', "")
    names = names.split(",")
    names.sort()
    answer = 0
    for i, name in enumerate(names):
        answer += score_count(name) * (i + 1)
    return answer


if __name__ == "__main__":
    print(score_count("colin"))
    print(euler_22())
