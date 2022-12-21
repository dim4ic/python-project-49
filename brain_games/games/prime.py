from random import randint

THE_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def function():

    question = randint(2, 30)
    count = 2

    while count <= question - 1:

        if question % count == 0:
            answer = 'no'
            break
        count += 1

    else:
        answer = 'yes'

    return str(answer), question
