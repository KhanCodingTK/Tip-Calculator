print("Welcome to tip calculator.")
total_bill = input("What was the total bill? $")
total_bill1 = int(total_bill)
tip_per = input("What percentage of the tip would you like to give?\n10, 12 or 15")
tip_per1 = int(tip_per)
total_people = input("How many people to split the bill?")
total_people1 = int(total_people)
tip_percentage = tip_per1/100
tip_percentage1 = total_bill1*tip_percentage
payment = (total_bill1+tip_percentage1)/total_people1
print(f"Each person should pay: ${payment}")
