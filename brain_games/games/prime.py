import random


def is_prime(number):
    if number < 2:
        return False
    
    # Check divisors from 2 to sqrt(number)
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    
    return True


def get_round_data():
    description = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    
    number = random.randint(1, 100)
    
    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    question = str(number)
    
    return description, question, correct_answer