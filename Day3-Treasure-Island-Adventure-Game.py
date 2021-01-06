print("Welcome to Treasure Island.")
print("Your mission is to find the reasure.")

directionOne = input("Left or Right? ")

if directionOne == "Left":
    swimConfirm = input("Swim or Wait? ")
    if swimConfirm == "Wait":
        colorDoor = input("Which door? Red, Blue, or Yellow? ")
        if colorDoor == "Yellow":
            print("You won!")
        elif colorDoor == "Blue":
            print("You picked the Blue door, Game Over.")
        elif colorDoor == "Red":
            print("You picked the Red door, Game Over.")
    else:
        print("Game Over. You should've waited.")
else:
    print("Game Over. You should've gone Left.")