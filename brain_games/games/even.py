import random


def get_round_data():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    number = random.randint(1, 100)
    question = str(number)
    if number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return description, question, correct_answer