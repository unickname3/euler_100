from utils import timer


class LetterCounter:
    letter_in_digit_spell = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    letter_in_tens_spell = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

    @classmethod
    def count_letter_in_number_spell(cls, number):
        len_of_phrase = 0
        hundreds = number // 100
        tens = number % 100

        if number == 1000:
            return 11
        if hundreds > 0:
            len_of_phrase += cls.letter_in_digit_spell[hundreds] + 7
            if tens != 0:
                len_of_phrase += 3
        if tens > 19:
            len_of_phrase += (
                cls.letter_in_tens_spell[tens // 10]
                + cls.letter_in_digit_spell[tens % 10]
            )
        else:
            len_of_phrase += cls.letter_in_digit_spell[tens]

        return len_of_phrase


@timer
def euler_17():
    return sum(map(LetterCounter.count_letter_in_number_spell, range(1, 1001)))


if __name__ == "__main__":
    print(euler_17())
