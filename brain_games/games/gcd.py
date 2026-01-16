import random


def get_round_data():
   
    description = "Find the greatest common divisor of given numbers."
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    a = num1
    b = num2
    
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    
    result = a
    question = f"{num1} {num2}"
    
    return description, question, str(result)