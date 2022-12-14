from random import randint
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    number1 = randint(0, 20)
    number2 = randint(0, 20)
    question = f'{number1} {number2}'
    correct_answer = math.gcd(number1, number2)

    return str(correct_answer), question
