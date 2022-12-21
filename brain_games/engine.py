import prompt

NUMBER_OF_ROUND = 3


def run_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.THE_TASK)

    counter = 1

    while counter <= NUMBER_OF_ROUND:
        correct_answer, question = game.make_game()
        print(f'Question: {question}')
        answer = prompt.string('You answer: ')

        if answer == correct_answer:
            print('Correct!')
            counter += 1

        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
