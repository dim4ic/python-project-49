from random import randint, choice

game = 'What number is missing in the progression?'


def function():
    length = randint(5, 10)
    start = randint(1, 5)
    step = randint(2, 5)
    progression = list(range(start, start + length * step, step))

    answer = choice(progression)
    question = ' '.join(
        '..' if number == answer else str(number) for number in progression
    )
    return str(answer), question
