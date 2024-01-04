from utils import timer


def calculate_word_value(word):
    value = 0
    for char in word:
        value += ord(char) - ord("A") + 1
    return value


def create_triangle_numbers_list(n):
    triangle_numbers_list = []
    for i in range(n + 1):
        triangle_numbers_list.append(i * (i + 1) // 2)
    return triangle_numbers_list


@timer
def euler_42():
    with open("0042_words.txt", "r") as input_file:
        input_data = input_file.read().replace('"', "")
        words_list = input_data.split(",")

    triangle_numbers_list = create_triangle_numbers_list(26 * 20)
    result = 0
    for word in words_list:
        num = calculate_word_value(word)
        if num in triangle_numbers_list:
            result += 1
    return result


if __name__ == "__main__":
    print(euler_42())
