import prompt


def run_game(get_round_data):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    
    rounds_count = 3

    for i in range(rounds_count):
        if i == 0:
            description, question, correct_answer = get_round_data()
            print(description)
        else:
            _, question, correct_answer = get_round_data()
        
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()

        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")