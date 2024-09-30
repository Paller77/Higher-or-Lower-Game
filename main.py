
#Importing from other modules:
import random
from art import logo
from art import vs
from game_data import data

# Function definition:
def format_data(account):
    """This function formats the dictionary to a readable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """This function compares the user's answer"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0

# Initial values:
play_again = True
is_game_over = False
account_b = random.choice(data)

# The 1st while loop loops the code as long as the player wants to replay
while play_again:
    #The 2nd while loops through the user's inputs as long as their answer is correct
    while not is_game_over:
        account_a = account_b
        account_b = random.choice(data)
        # This if block does not allow to duplicate
        if account_a == account_b:
            account_b = random.choice(data)
        # Printing out the chosen data in readable format
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")

        # Asking for a guess:
        guess = input("Who has more followers A or B?\n").lower()

        print("\n" * 50)
        print(logo)

        # Receiving the number of followers for the chosen account
        a_follower_num = account_a["follower_count"]
        b_follower_num = account_b["follower_count"]

        # Checking if the answer is correct
        is_correct = check_answer(guess, a_follower_num, b_follower_num)

        # If the answer is okay then score + 1, else the game is over:
        if is_correct:
            score += 1
            print(f"That's correct! Your current score: {score}")
        else:
            print(f"You're wrong! Final score: {score}")
            is_game_over = True

    # Checking if the player wants to replay:
    another_game = input("Do you want to play again? 'Y' or 'N'\n").lower()

    # If yes, then reset progress and start the game over again, else exit.
    if another_game == "y":
        play_again = True
        is_game_over = False
        score = 0
        account_b = random.choice(data)
        if account_a == account_b:
            account_b = random.choice(data)
        print("\n" * 50)
        print(logo)

    else:
        play_again = False