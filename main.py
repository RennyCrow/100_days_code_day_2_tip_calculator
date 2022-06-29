print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

percentage = percentage_tip / 100
bill +=  bill * percentage
#payment = round(bill / people, 2)
#Using the format function to specify that I want to use two decimal places even though last value be 0
payment = "{:.2f}".format(bill / people, 2) 

print(f"Each person should pay: ${payment}")