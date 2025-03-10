print("your mission is to find the treasure.")
c1 = input('you reach a crossroad, where do you want to go ? '
                'type "left" or "right".\n').lower()

if c1 == "left":
    c2 = input('you come across a lake. '
                    'there is an island in the middle of the lake. '
                    'type "wait" to wait for a boat. '
                    'type "swim" to swim across.\n').lower()
    if c2 == "wait":
        c3 = input("you arrive at the island unharmed. "
                        "there is house with 3 doors. one red, "
                        "one yellow and one blue. "
                        "which colour do you choose?\n").lower()
        if c3 == "red":
            print("it's a room full of fire. Game Over")
        elif c3 == "yellow":
            print("you found the treasure. You Win!")
        elif c3 == "blue":
            print("you enter a room of beasts. Game Over.")
        else:
            print("you chose a door that doesn't exist. Game Over.")
    else:
        print("you got attacked by an angry trout. Game Over.")

else:
    print("you fell in to a hole. Game Over.")
