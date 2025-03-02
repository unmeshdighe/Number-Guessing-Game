import random
import time

def intro():
    print("May I ask you for your name?")
    name = input()  # Ask for the player's name
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def pick(number, name):
    guesses_taken = 0
    while guesses_taken < 6:  # Allow up to 6 guesses
        time.sleep(0.25)
        enter = input("Guess: ")  # Prompt for the guess

        try:
            guess = int(enter)  # Convert the input to an integer

            if 1 <= guess <= 200:  # Check if the guess is within the valid range
                guesses_taken += 1  # Increment the guess count

                if guess < number:
                    print("The guess of the number that you have entered is too low.")
                elif guess > number:
                    print("The guess of the number that you have entered is too high.")
                else:
                    print(f'Good job, {name}! You guessed my number in {guesses_taken} guesses!')
                    return  # Exit the function if the guess is correct

                if guesses_taken < 6:
                    time.sleep(0.5)
                    print("Try Again!")
            else:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 200.")

        except ValueError:  # Handle non-integer inputs
            print(f"I don't think that '{enter}' is a number. Sorry.")

    # If the player runs out of guesses
    print(f'Nope. The number I was thinking of was {number}.')

def main():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:  # Allow for case-insensitive input
        number = random.randint(1, 200)  # Generate a random number between 1 and 200
        name = intro()  # Get the player's name
        pick(number, name)  # Start the guessing game
        print("Do you want to play again? (yes/no)")
        play_again = input()

if __name__ == "__main__":
    main()
