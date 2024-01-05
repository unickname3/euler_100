from datetime import date, timedelta

from utils import timer


def next_sunday_generator(interested_date: date) -> date:
    while interested_date.weekday() != 6:
        interested_date += timedelta(days=1)
        yield interested_date
    while True:
        interested_date += timedelta(days=7)
        yield interested_date


def count_sunday(start: date, end: date) -> int:
    result = 0
    sunday_generator = next_sunday_generator(start)
    while (sunday := next(sunday_generator)) < end:
        if sunday.day == 1:
            result += 1
    return result


@timer
def euler_19():
    return count_sunday(
        date(year=1901, day=1, month=1), date(year=2000, month=12, day=31)
    )


if __name__ == "__main__":
    print(euler_19())
