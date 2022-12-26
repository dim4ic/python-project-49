from random import randint

TASK = 'What number is missing in the progression?'


def generate_progression(start, length, step):
    return list(range(start, start + length * step, step))


def make_round():
    length = randint(5, 10)
    start = randint(1, 5)
    step = randint(2, 5)
    question = generate_progression(start, length, step)

    hidden_index = randint(0, len(question) - 1)
    correct_answer = str(question[hidden_index])
    question[hidden_index] = '..'
    question = ' '.join(str(i) for i in question)

    return str(correct_answer), str(question)
