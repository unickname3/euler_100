from utils import timer, get_primes_list


def sum_of_proper_divisors(number: int) -> int:
    result = 1
    for k in range(2, int(number**0.5) + 1):
        if number % k == 0:
            result += k + number // k
    return result


@timer
def euler_21() -> int:
    # primes = get_primes_list(less_than=10000)
    answer = 0
    d_dict = {}
    for number in range(10000):
        sum_of_pd = sum_of_proper_divisors(number)
        if sum_of_pd in d_dict.keys():
            if d_dict[sum_of_pd] == number:
                answer += number + sum_of_pd
        d_dict[number] = sum_of_pd
    return answer


if __name__ == "__main__":
    print(euler_21())
