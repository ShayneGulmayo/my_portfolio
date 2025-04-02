print("Gulmayo, Shayne Marie F.")
print("2BSIT-2\n")

name = input("Enter student’s name (LN, FN MI): ")
print("Enter student's grade in")
math = input("\tMath: ")
science = input("\tScience: ")
english = input("\tEnglish: ")

average = (int(math) + int(science) + int(english))/3

text1 = "Average grade of %s is %.2f" % (name, average)
print(text1)

