import random
from game_data import data
from art import logo, vs

def random_account():
    return random.choice(data)

def format_account(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name},a {description},from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

score = 0
should_continue = True
account_a = random_account()
account_b = random_account()

while account_a == account_b:
    account_b = random_account()

while should_continue:
    print(logo)
    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B':")

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")

        account_a = account_b
        account_b = random_account()
        while account_a == account_b:
            account_b = random_account()
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")


