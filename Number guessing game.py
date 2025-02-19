import random
import datetime

def guess(chance):
    random_number = random.randint(1, 100)
    guessed_correctly = False
    end_time = ''
    start_time = datetime.datetime.now()

    for i in range(1, chance+1):
        try:
            user_input = int(input("Enter your guess: "))
            if user_input == random_number:
                guessed_correctly = True
                end_time = datetime.datetime.now()
                break
            elif user_input < random_number:
                print(f"Incorrect! The number is greater than {user_input}.")
            else:
                print(f"Incorrect! The number is less than {user_input}.")
            print("\n")
        except ValueError:
            print("Problem with the input value, try again.")
            exit()
        
    if guessed_correctly == False:
        print("Sorry, you couldn't guess the number, better luck next time.\n")
        print(f"The number was: {random_number}\n")
    else:
        print(f"\nCongratulations! You guessed the correct number in {i} attempts.")
        print(f"Time taken: {(end_time - start_time).total_seconds()} seconds.\n")
    
def print_instructions():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.\n")
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("\n")

def difficulty_level():
    try:
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            print("Great! You have selected the Easy difficulty level.")
            return 10
        elif user_input == 2:
            print("Great! You have selected the Medium difficulty level.")
            return 5
        elif user_input == 3:
            print("Great! You have selected the Hard difficulty level.")
            return 3
        else:
            print("please choose a input from the mentioned range.")
            return difficulty_level()
    except ValueError:
        print("Problem with the input value, try again.\n")
        return difficulty_level()

if __name__=='__main__':
    while True:
        print_instructions()
        number_of_chance = difficulty_level()
        print("Let's start the game!\n")
        guess(number_of_chance)

        replay = input("Would you like to play again? (type 'yes' to continue playing): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing, Goodbye.")
            break

    
    
    


"""
### INSTUCTIONS
Number Guessing Game

You are required to build a simple number guessing game where the computer randomly selects a number and the user has to guess it. The user will be given a limited number of chances to guess the number. If the user guesses the number correctly, the game will end, and the user will win. Otherwise, the game will continue until the user runs out of chances.

Requirements
It is a CLI-based game, so you need to use the command line to interact with the game. The game should work as follows:

When the game starts, it should display a welcome message along with the rules of the game.
The computer should randomly select a number between 1 and 100.
User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
The user should be able to enter their guess.
If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than the user’s guess.
The game should end when the user guesses the correct number or runs out of chances.
"""