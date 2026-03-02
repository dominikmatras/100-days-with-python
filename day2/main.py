print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How mach tip would you like to give? 10, 12 or 15%: "))
people = int(input("How many people to split the bill? "))
total_bill_with_tip_per_person = (bill + (bill / tip)) / people
print(f"Each person shoud pay: ${round(total_bill_with_tip_per_person, 2)}")