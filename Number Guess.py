import random

print("Welcome to the Number Guessing Game!\n")
number_to_guess = random.randint(1, 10)
attempts = 3
print("I'm thinking of a random number between 1 and 10 can you guess it? \n you have 3 attempts")
for attempt in range(1, attempts + 1):
    guess = int(input("\nEnter your guess between (1-10) :"))
    if guess < number_to_guess:
        print("\nYour guess is too low.")
    elif guess > number_to_guess:
        print("\nYour guess is too high.")

    if guess < 1 or guess > 10:
        print("\nPlease guess a number within the range of 1 to 10.")
        continue 
    if guess == number_to_guess:
        print(f"Congratulations! You've guessed the number {number_to_guess} correctly!\n")
        print("Thank you for playing the Number Guessing Game. Goodbye!")
        break 
    else:
        print("\nWrong guess. Try again.")
else:
    print(f"\nSorry, you've used all your attempts. The correct number was {number_to_guess}.")
    print("Thank you for playing the Number Guessing Game. Goodbye!")