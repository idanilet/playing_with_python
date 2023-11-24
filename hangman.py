import random


def choose_word():
    words = ["python", "java", "javascript", "ruby", "programming", "developer", "computer", "algorithm"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""  # creates an empty string
    for letter in word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "
    return display


def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to 'Hangman' game!")
    print(display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters) and attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed this letter.")
            elif guess in word_to_guess:
                guessed_letters.append(guess)
                print("Correct!")
            else:
                guessed_letters.append(guess)
                attempts -= 1
                print(f"The letter is not part of the word. You have {attempts} attempts left.")
        else:
            print("Please type a valid letter..")

        print(display_word(word_to_guess, guessed_letters))

    if "_" not in display_word(word_to_guess, guessed_letters):
        print(f"Congratulations, you've guessed the word: {word_to_guess}")
    else:
        print(f"You lost. The correct word was: {word_to_guess}")


hangman()
