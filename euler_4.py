from utils import timer


def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


def get_palindromes(k, edge):
    palindromes = set()
    for a in range(k, k - edge, -1):
        for b in range(k, k - edge, -1):
            n = a * b
            if is_palindrome(n):
                palindromes.add(n)
    return palindromes


@timer
def euler_4():
    a = 999
    b = 999
    edge = 2
    while edge < 10**6:
        palindromes = get_palindromes(1000, edge)
        if len(palindromes):
            return max(palindromes)
        edge *= 2


if __name__ == "__main__":
    print(euler_4())
