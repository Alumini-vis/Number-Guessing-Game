import random

def number_guessing_game(attempts):
    """
    The number guessing game is a logic puzzle where the player has to guess a randomly generated 
    number between 1 and 100. The player has a limited number of attempts to guess the correct number

    Returns:
        str: A message indicating whether the player has won or lost the game.

    """

    # Generate a random number between 1 and 100.
    guess = random.randint(1,100)

    print("Welcome to the Number Guessing Game!")
    print("You have {} attempts to guess the number between 1 and 100.".format(attempts))

    for i in range(attempts):
        # Get the player's guess.
        player_guess = int(input("Enter your guess: "))

        # Check if the player's guess is correct.
        if player_guess == guess:
            print("Congratulations! You've guessed the correct number!" .format(player_guess))
            return "You won the guessing game!"
        elif player_guess < guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    return "Sorry, you've used all your attempts. The correct number was {}.".format(guess)

if __name__ == '__main__':
    # Start by asking the player the number of attempts or by default.
    print(number_guessing_game(int(input("Enter the number of attempts you want (default is 7):"))))