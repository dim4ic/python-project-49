from random import randint

THE_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_game():

    question = randint(2, 30)
    count = 2

    while count <= question - 1:

        if question % count == 0:
            correct_answer = 'no'
            break
        count += 1

    else:
        correct_answer = 'yes'

    return str(correct_answer), question
