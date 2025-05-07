import random


def number_gussing_game():
    print("Welcome to the Number Gussing Game!🎯")

    Scret_number = random.randint(1, 5)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10:"))
            attempts += 1

            if guess < Scret_number:
                print("Too low, try again!")
            elif guess > Scret_number:
                print("Too high, try again!")
            else:
                print(f"Congratulations! You guessed the number {guess} = {Scret_number} in {attempts} attempts. 🎉")
                break
        except ValueError:
            print("Please enter a valid number.")



# Run the game
number_gussing_game()
            





           
        