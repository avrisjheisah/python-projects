print("welcome to the tip calculator!")
bill = float((input("whats the total ? $")))
print(bill)
tip = int(input("how much tip would you like to give ? 10,12 or 15? "))
print(tip)
split = int(input("splitting how many ways ? "))
print(split)
person = (bill + ((tip/100)*bill))/split
print(f"each person pays : ${round(person,2)}" )