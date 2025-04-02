print("Gulmayo, Shayne Marie F.")
print("2BSIT-2\n")

print("Nouns")
noun1 = input("Enter the first noun: ")
noun2 = input("Enter the second noun: ")
noun3 = input("Enter the third noun: ")
print("-----------------------------")
print("Adjectives")
adj1 = input("Enter the first adjective: ")
adj2 = input("Enter the second adjective: ")
adj3 = input("Enter the third adjective: ")
print("-----------------------------")
print("Original Song")
print("This love is good\n"
      "This love is bad\n"
      "This love alive\n"
      "Back from the dead")
print("-----------------------------")
thisLove = ("This %s is %s\n"
      "This %s is %s\n"
      "This %s is %s\n"
      "Back from the dead") % (noun1.upper(), adj1.upper(), noun2.upper(), adj2.upper(), noun3.upper(), adj3.upper())
print("Edited Song")
print(thisLove)

