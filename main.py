import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

print(logo)
print("Welcome to Number Guessing Game")
print("I'm thinking of a number 1 to 100")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    turns = set_difficulty()
    computer_generated_num = random.randint(1, 100)
    is_game_over = False
    while not is_game_over:
        print(f"You have {turns} remaining to guess")
        user_guess_num = int(input("Make a guess: "))

        turns -= 1
        if turns == 0:
            print(f"You lose the game 😭, correct guess is: {computer_generated_num}")
            break

        if user_guess_num < computer_generated_num:
            print("To low ⬇️")
            print("Try again 🤨")
        elif user_guess_num > computer_generated_num:
            print("To high ⬆️")
            print("Try again 🤨")
        elif user_guess_num == computer_generated_num:
            is_game_over = True
            print("Your guess is correct 🥳, you won")


game()
