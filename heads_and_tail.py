import random

options = ['head', 'tails']

flip = True

while flip:
    user_input = input("Flip? (y/n)\n").lower()

    if user_input == 'n':
        print("Byeee! :(")
        flip = False
    elif user_input == 'y':
        answer = input("Heads or tails? (head/tails)\nAnswer: ").lower()
        result = random.choice(options)
        print("Result:", result)
        if answer == result:
            print("You win!\n")
        else:
            print("Better luck next time! :)\n")
    else:
        print("Invalid input. Please enter 'y' or 'n'. ")
