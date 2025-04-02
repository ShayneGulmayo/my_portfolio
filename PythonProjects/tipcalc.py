#Activity 1

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? P"))
percent = float(input("What percentage tip would you like to give? 10 12 15 "))
percent = (percent * 0.01) + 1
people = float(input("How many people to split the bill? "))


payment = (total/people) * percent

print(f"Each person should pay: {round(payment, 2)}")
