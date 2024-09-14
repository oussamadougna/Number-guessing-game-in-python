import random
import math

def guessing_game():
    lower = int(input("Enter the first number: "))
    upper = int(input("Enter the second number (greater than the first): "))

    if upper <= lower:
        print("The upper bound must be greater than the lower bound.")
        return

    total_chances = math.ceil(math.log2(upper - lower + 1))
    print(f"You have only {total_chances} chances to guess the number.")

    guess = random.randint(lower, upper)
    count = 0
    flag = False

    while count < total_chances:
        player_guess = int(input(f"Enter your guess (between {lower} and {upper}): "))
        count += 1

        if player_guess == guess:
            print(f"Congratulations! You guessed the number in {count} tries.")
            flag = True
            break
        elif player_guess < guess:
            print("Your guess is too low!")
        elif player_guess > guess:
            print("Your guess is too high!")

    if not flag:
        print(f"The number was {guess}.")
        print("Better luck next time!")

if __name__ == "__main__":
    guessing_game()
