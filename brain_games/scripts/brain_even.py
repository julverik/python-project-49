import random
import prompt
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def get_answer(number):
    if is_even(number):
        return 'yes'
    else:
        return 'no'


def run_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_count = 3

    for _ in range(rounds_count):
        number = random.randint(1, 100)
        print(f'Question: {number}')
        
        user_answer = prompt.string('Your answer: ').strip().lower()

        correct_answer = get_answer(number)

        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print('Correct!')

    print(f'Congratulations, {name}!')


def main():
    run_even_game()


if __name__ == "__main__":
    main()