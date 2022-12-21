from random import randint, choice

THE_TASK = 'What number is missing in the progression?'


def make_game():
    length = randint(5, 10)
    start = randint(10, 30)
    step = randint(2, 5)
    progression = list(range(start, start + length * step, step))

    correct_answer = choice(progression)
    question = progression
    for i in range(len(question)):
        question[i] = str(question[i])

    question = ' '.join(question)
    question = question.replace(str(correct_answer), '..')

    return str(correct_answer), question
