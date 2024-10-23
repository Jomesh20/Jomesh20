print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#To calculate tip
new_tip = bill * (tip / 100)

#To calculate final amont
total_bill = (bill + new_tip) / people

#To round up total bill to 2 decimal places
final_bill = "{:.2f}".format(round(total_bill, 2))

print(f"Each person should pay: ${final_bill}")