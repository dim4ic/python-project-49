from random import randint


THE_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(value):
    return value % 2 == 0


def make_game():
    question = randint(0, 20)

    if even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return str(correct_answer), question
