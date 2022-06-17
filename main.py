import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        print(f'Guess a number between 1 and {x}')
        guess = int(input())
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print("You got it!")
            break

guess(10)