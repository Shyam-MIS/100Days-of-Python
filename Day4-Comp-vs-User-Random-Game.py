import random

userChoice = int(input("What do you choose? Choose 0 or 1 or 2 "))
computerChoice = random.randint(0,2)

if userChoice == computerChoice:
    print("Draw!")
elif userChoice < computerChoice:
    print("Computer Won!")
else:
    print("You won!")