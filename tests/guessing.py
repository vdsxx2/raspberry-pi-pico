import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the number of guesses
num_guesses = 5

# Loop until the player guesses the number or runs out of guesses
while num_guesses > 0:
    # Get a guess from the player
    guess = int(input("Guess a number between 1 and 100: "))

    # Decrement the number of guesses
    num_guesses -= 1

    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations, you guessed the number! 👑")
        break
    elif guess < secret_number:
        print("Too low!📉 You have", num_guesses, "guesses left.")
    else:
        print("Too high!📈 You have", num_guesses, "guesses left.")

# If the player runs out of guesses, reveal the number
if num_guesses == 0:
    print("Sorry, you ran out of guesses. The number was", secret_number)


