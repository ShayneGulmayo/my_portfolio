def reverse(word):

    print("STRING: " + word)
    rev = word[::-1]
    element = len(rev)
    print("REVERSED: " + rev.upper() + " (" + str(element) + " characters)")

print("Gulmayo, Shayne Marie F.")
print("2BSIT-2\n")

word = input("Enter word/s: ")
reverse(word)