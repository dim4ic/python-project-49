from random import randint, choice

THE_TASK = 'What is the result of the expression?'


def calculation(number1, number2, operator):
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    elif operator == '*':
        answer = number1 * number2
    return answer


def make_game():
    list = ['+', '-', '*']
    operator = choice(list)
    number1 = randint(0, 10)
    number2 = randint(0, 10)
    correct_answer = calculation(number1, number2, operator)
    question = f'{number1} {operator} {number2}'

    return str(correct_answer), question
