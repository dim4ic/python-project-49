import random
from random import randint

THE_TASK = 'What is the result of the expression?'


def make_game():

    number1 = randint(0, 10)
    number2 = randint(0, 10)
    a = f'{number1} + {number2}'
    a_answer = number1 + number2
    b = f'{number1} - {number2}'
    b_answer = number1 - number2
    c = f'{number1} * {number2}'
    c_answer = number1 * number2

    list = [a, b, c]
    question = random.choice(list)

    if question == a:
        correct_answer = a_answer
    elif question == b:
        correct_answer = b_answer
    elif question == c:
        correct_answer = c_answer

    return str(correct_answer), question
