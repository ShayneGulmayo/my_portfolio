print("Gulmayo, Shayne Marie F.")
print("2BSIT-2\n")

words = []
choice = 'y'

while choice.casefold() == 'y':
    word = input("Enter a word: ")
    words.append(word)
    print("You entered the word", word)
    choice = input("Do you want to try again? Y/N ")
    if choice.casefold() == 'n':
        break


length = len(words)
print("You entered", length, "words")
for i in range(length):
    print(words[i])
