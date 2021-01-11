import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


generatedPass = ""
letterCount = len(letters)
numberCount = len(numbers)
symbolCount = len(symbols)


for letter in range(0, nr_letters):
    testLetterPass = letters[random.randint(0,letterCount-1)]
    generatedPass += testLetterPass

for symbol in range(0, nr_symbols):
    testSymbolPass = symbols[random.randint(0,symbolCount-1)]
    generatedPass += testSymbolPass

for number in range(0, nr_numbers):
    testNumberPass = numbers[random.randint(0,numberCount-1)]
    generatedPass += testNumberPass


print("Your pass is: " + generatedPass)