import random

rock = 'o'
paper = '//'
scissors = 'y'

choices = [rock, paper, scissors]

user_choice = int(input("type 0 for rock, 1 for paper or 2 for scissors.\n"))

if user_choice >= 0 and user_choice <= 2:
    print(choices[user_choice])

computer_choice = random.randint(0, 2)
print("computer chose:")
print(choices[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you typed an invalid number. you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("you lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a draw!")

