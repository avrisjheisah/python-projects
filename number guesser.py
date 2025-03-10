from random import randint
from art import logo

ezturn = 10
hardturn = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("too low.")
        return turns - 1
    else:
        print(f"you got it! the answer was {actual_answer}")



def set_difficulty():
    level = input("choose a difficulty. type 'easy' or 'hard': ")
    if level == "easy":
        return ezturn
    else:
        return hardturn


def game():
    print(logo)
    print("the number to guess is between 1 and 100")
    answer = randint(1, 100)
    print(f"the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("guess again.")


game()
