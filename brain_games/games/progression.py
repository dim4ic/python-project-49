from random import randint, choice

THE_TASK = 'What number is missing in the progression?'


def progression(start, length, step):
    return list(range(start, start + length * step, step))


def make_game():
    length = randint(5, 10)
    start = randint(1, 5)
    step = randint(2, 5)
    question = progression(start, length, step)

    correct_answer = choice(question)
    index = 0
    for number in question:
        if number == correct_answer:
            question[index] = '..'
        else:
            str(number)
            index += 1

    question = ' '.join(str(i) for i in question)

    return str(correct_answer), question
