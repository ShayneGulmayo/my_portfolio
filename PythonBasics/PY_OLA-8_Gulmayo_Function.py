def avrg(name, math, english, science):

    math = float(math)
    english = float(english)
    science = float(science)
    ave = (math + english + science)/3

    print()
    print(name)
    print("\tMath: " + str(math) + ", English: " + str(english) + ", Science: " + str(science))
    print("\tAverage: ", ave)
    print()

print("Gulmayo, Shayne Marie F.")
print("2BSIT-2\n")

choice = 'y'

while choice.casefold() == 'y':
    name = input("Enter Student Name: ")
    math = input("Enter Math Grade: ")
    english = input("Enter English Grade: ")
    science = input("Enter Science Grade: ")
    avrg(name, math, english, science)
    choice = input("Do you want to add more? Y/N ")
    if choice.casefold() == 'n':
        break


