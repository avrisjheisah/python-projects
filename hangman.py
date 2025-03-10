import random


def get_random_word():
    words = ["python", "hangman", "programming", "challenge", "computer"]
    return random.choice(words)


def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def play_hangman():
    word = get_random_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")


    while tries > 0 and word_letters:
        print(display_hangman(6 - tries))
        print("guessed letters:", " ".join(sorted(guessed_letters)))

        current_word = [letter if letter in guessed_letters else "_" for letter in word]
        print("word: ", " ".join(current_word))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("you already guessed that letter. try again.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("good guess!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"wrong guess. tries left: {tries}")

        print("\n")

    if not word_letters:
        print("congratulations! you guessed the word:", word)
    else:
        print(display_hangman(6 - tries))
        print("sorry, you ran out of tries. the word was:", word)


if __name__ == "__main__":
    play_hangman()
