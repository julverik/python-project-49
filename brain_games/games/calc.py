import random


def get_round_data():
    description = "What is the result of the expression?"
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    
    match operation:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
    
    question = f"{a} {operation} {b}"
    return description, question, result