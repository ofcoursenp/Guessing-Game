
import random


def start_game():
    secret_number = random.randint(0, 10)
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        guess = int(input('Guess: '))
        guess_count += 1

        if guess == secret_number:
            print("Congrats, You Won!")
            again = input('Do you want to play again? "y" or "n": ').lower()

            if again == 'y':
                start_game()
            elif again == 'n':

                exit()
            else:
                print("I don't understand that.")
                break

        elif guess_count == guess_limit and guess != secret_number:

            print("Sorry, You Failed!")
            again = input('Do you want to play again? "y" or "n": ').lower()

            if again == 'y':
                start_game()

            elif again == 'n':
                exit()

            else:
                print("I don't understand that.")
                break

        else:
            print('Try again!')


start_game()

