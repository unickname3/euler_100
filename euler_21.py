from utils import timer, sum_of_proper_divisors


@timer
def euler_21() -> int:
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
