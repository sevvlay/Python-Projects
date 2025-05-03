from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, correct_answer, turns_remaining):
    """Checks the user's guess against the correct answer."""
    if user_guess > correct_answer:
        print("Too High.")
        return turns_remaining - 1
    elif user_guess < correct_answer:
        print("Too Low.")
        return turns_remaining - 1
    else:
        print(f"You got it! The answer was {correct_answer}.")

def choose_difficulty():
    """Asks the user to choose a difficulty level."""
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if level == 'easy':
            return EASY_LEVEL_TURNS
        elif level == 'hard':
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please type 'easy' or 'hard'.")

def get_valid_guess():
    """Prompts the user for a valid integer guess."""
    while True:
        guess = input("Make a guess: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Please enter a valid number.")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    correct_answer = randint(1, 100)
    turns_remaining = choose_difficulty()

    while True:
        print(f"You have {turns_remaining} attempts remaining to guess the number.")
        user_guess = get_valid_guess()

        turns_remaining = check_answer(user_guess, correct_answer, turns_remaining)

        if user_guess == correct_answer:
            break
        elif turns_remaining == 0:
            print(f"You've run out of guesses, you lose. The answer was {correct_answer}")
            break
        else:
            print("Guess again.")

game()
