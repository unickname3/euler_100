from utils import timer


def variants_generator(num, generated_list, result_set):
    if len(generated_list) == 9:
        next_generated_list = generated_list.copy()
        next_generated_list.append(num)
        result_set.add(tuple(next_generated_list))
        return True
    for i in range(num + 1):
        next_generated_list = generated_list.copy()
        next_generated_list.append(i)
        variants_generator(num - i, next_generated_list, result_set)


def squares_chain(num, list_of_squares):
    squares_sum = 0
    for digit in str(num):
        squares_sum += list_of_squares[int(digit)]
    if squares_sum == 0:
        return 0
    if squares_sum == 1:
        return 1
    elif squares_sum == 89:
        return 89
    else:
        return squares_chain(squares_sum, list_of_squares)


@timer
def euler_92():
    factorials_list = [1, 1]
    for i in range(2, 8):
        factorials_list.append(factorials_list[i - 1] * i)

    list_of_squares = [x**2 for x in range(10)]

    result_set = set()
    num_of_digits = 7
    variants_generator(num_of_digits, [], result_set)
    print(result_set)
    result = 0
    for el in result_set:
        multiplier = factorials_list[7]
        squares_sum = 0
        for i in range(10):
            multiplier /= factorials_list[el[i]]
            squares_sum += list_of_squares[i] * el[i]
        if squares_chain(squares_sum, list_of_squares) == 89:
            result += multiplier
    return int(result)


if __name__ == "__main__":
    print(euler_92())
