import random
number= random.randint(1, 10)
guesses = 0
while guesses !=number:
    guesses = int(input("Guess a number between 1 and 10: "))
    if guesses < number:
        print("Too low! Try again.")
    elif guesses > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number:", number)
        break
print("Game Over!")