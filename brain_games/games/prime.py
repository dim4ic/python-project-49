from random import randint

THE_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    count = 2

    while count <= question // 2:

        if question % count == 0:

            return True
            break
        count += 1


def make_game():

    question = randint(2, 30)
    if is_prime(question):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return str(correct_answer), question
