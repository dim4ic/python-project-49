from random import randint


THE_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_game():

    question = randint(0, 20)
    if question % 2 == 0:
        correct_answer = 'yes'

    elif question % 2 != 0:
        correct_answer = 'no'

    return correct_answer, question
