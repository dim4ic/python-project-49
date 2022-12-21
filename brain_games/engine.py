import prompt


def run_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.THE_TASK)

    counter = 1

    while counter <= 3:
        answer, question = game.function()
        print(f'Question: {question}')
        my_answer = prompt.string('You answer: ')

        if my_answer == answer:
            print('Correct!')
            counter = counter + 1

        elif my_answer != answer:
            print(
                f'{my_answer} is wrong answer ;(. Correct answer was {answer}.')
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
