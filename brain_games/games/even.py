from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    return value % 2 == 0


def make_round():
    question = randint(0, 20)

    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(correct_answer), str(question)
