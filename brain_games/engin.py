import prompt


def run_game(name_game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    game = name_game.game
    print(game)

    counter = 1

    while counter <= 3:
        answer, question = name_game.function()
        print(f'Question: {question}')
        user_answer = prompt.string('You answer: ')

        if user_answer == answer:
            print('Correct!')
            counter = counter + 1

        elif user_answer != answer:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {answer}.')
            print(f'Lets try again, {name}!')
            return

    print(f'Congratulations, {name}!')