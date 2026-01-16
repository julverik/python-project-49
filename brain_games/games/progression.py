import random


def get_round_data():
    description = "What number is missing in the progression?"
    
    start = random.randint(1, 50)        
    step = random.randint(1, 10)          
    length = random.randint(5, 10)       
    
    progression = []
    for i in range(length):
        current = start + i * step
        progression.append(str(current))
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(progression)
    
    return description, question, correct_answer