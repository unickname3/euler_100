from utils import timer, sum_of_proper_divisors


@timer
def euler_23() -> int:
    answer = 0
    abudant_numbers = set()
    for number in range(1, 28123):
        if sum_of_proper_divisors(number) > number:
            abudant_numbers.add(number)
        for k in abudant_numbers:
            if number - k in abudant_numbers:
                break
        else:
            answer += number
    return answer


if __name__ == "__main__":
    print(euler_23())
