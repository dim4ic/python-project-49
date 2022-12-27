from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question < 2:
        return is_prime(question)
    count = 2
    while count <= question // 2:
        if question % count == 0:
            return True
        count += 1
    return False


def generate_round():

    question = randint(0, 30)
    if is_prime(question):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return correct_answer, str(question)
