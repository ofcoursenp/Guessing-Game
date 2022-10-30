
import random


def start_game(upperbound):
    secret_number = random.randint(1, upperbound)
    guess_count = 0
    guess_limit = 3

    while guess_count < guess_limit:
        guess = int(input('Guess: '))
        guess_count += 1

        if guess == secret_number:
            print("Congrats, You Won!")
            again = input('Do you want to play again? "y" or "n": ').lower()

            if again == 'y':
                upperbound = 0
                try:
                    upperbound = int(input("Enter upper bound : "))
                except ValueError:
                    print("")
                if upperbound > 0:
                    start_game(upperbound=upperbound)
                else:
                    print("I dont understand that ")
                    quit()

            elif again == 'n':
                exit()

            else:
                print("I don't understand that.")
                break

        if guess > secret_number:
            print("Go a bit low")

        if guess < secret_number:
            print("Go a bit high")


        if guess_count == guess_limit and guess != secret_number:

            print("Sorry, You Failed!")
            again = input('Do you want to play again? "y" or "n": ').lower()

            if again == 'y':
                upperbound = 0
                try:
                    upperbound = int(input("Enter upper bound : "))
                except ValueError:
                    print("Please enter correct value ")
                if upperbound > 0:
                    start_game(upperbound=upperbound)
                else:
                    print("I dont understand that ")
                    quit()

            elif again == 'n':
                exit()

            else:
                print("I don't understand that.")
                break

        else:
            print('Try again!')

upperboundcheck = True
while upperboundcheck:
    try:
        upperbound = 0
        upperbound = int(input("Enter upper bound : "))
    except ValueError:
        print("Please enter correct integer value ")
    if upperbound > 0:
        upperboundcheck = False

start_game(upperbound)
