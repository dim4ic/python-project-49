from random import randint
import math

THE_TASK = 'Find the greatest common divisor of given numbers.'


def function():
    number1 = randint(0, 20)
    number2 = randint(0, 20)
    question = f'{number1} {number2}'
    answer = math.gcd(number1, number2)

    return str(answer), question
