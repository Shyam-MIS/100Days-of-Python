#Tipping Calculator 
print("Welcome to the tip calculator.")

totalBill = float(input("What was the total bill? "))
percentageTip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
totalPeople = int(input("How many people are splliting the bill? "))

paymentCalc = ((totalBill * (percentageTip/100)) + totalBill) / totalPeople

print("Each person should pay: $" + str(round(paymentCalc, 2)))