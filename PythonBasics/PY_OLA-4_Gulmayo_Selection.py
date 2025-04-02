print("Gulmayo, Shayne Marie F.")
print("2BSIT-2\n")

print("=================================")
name = input("Enter employee name: ")
years = int(input("Enter years-in-service: "))
office = input("Enter office: ")
bonus = 0
if years <= 10:
    if office == "it":
        bonus = 5000
    elif office == "hr":
        bonus = 7500
    elif office == "acct":
        bonus = 6000
else:
    if office == "it":
        bonus = 10000
    elif office == "hr":
        bonus = 15000
    elif office == "acct":
        bonus = 12000

print("=================================\n")

text1 = "Hi %s, your bonus is %d." % (name, bonus)
print(text1)

