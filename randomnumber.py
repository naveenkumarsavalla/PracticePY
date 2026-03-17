# Random number
import random

x = random.randint(1,10)

while True:
    p = int(input("Enter value (1-10): "))

    if p == x:
        print("Congrats! You guessed correctly.")
        break
    else:
        print("Too high! Try again.")