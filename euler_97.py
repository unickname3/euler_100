from utils import timer


@timer
def euler_97():
    massive_non_Mersenne_prime = 28433 * pow(2, 7830457, 10000000000) + 1
    return str(massive_non_Mersenne_prime)[-10:]


if __name__ == "__main__":
    print(euler_97())
