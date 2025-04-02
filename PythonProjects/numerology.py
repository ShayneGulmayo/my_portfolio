numerology = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9,
              "j":1, "k":2, "l":3, "m":4, "n":5, "o":6, "p":7, "q":8, "r":9,
              "s":1, "t":2, "u":3, "v":4, "w":5, "x":6, "y":7, "z":8}

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

personality_chart = {1:"pioneering, leading, independent, attaining, individualistic",
                     2:"cooperation, adaptability, considering, partnering, mediating",
                     3:"expression, verbalization, socialization, arts, joy of living",
                     4:"values foundation, service, struggle against limits, steady growth",
                     5:"expansiveness, visionary, adventure, constructive use of freedom",
                     6:"responsibility, protection, nurturing, balance, sympathy",
                     7:"analysis, understanding, awareness, studious, meditating",
                     8:"practical endeavors, status oriented, power-seeking, high-material goals",
                     9:"humanitarian, giving, selflessness, obligations, creative expression",
                     11:"higher spiritual plane, intuitive, illumination, idealist, a dreamer",
                     22:"master builder, large endeavors, powerful force, leadership",
                     33:"master builder, large endeavors, powerful force, leadership"}

destiny_chart = {1:"Primal Force", 2:"All Knowing", 3:"Creative Child", 4:"Salt of the Earth",
                5:"Dynamic Force", 6:"The Caretaker", 7:"The Seeker", 8:"Balance and Power", 9:"The Caretaker",
                11:"The Intuitive", 22:"Master Builder", 33:"Master Teacher"}

name_vwls = []
name_cons = []
name_destiny = []


def reduce(num, allow=True):
    sums = [num]
    if allow and num in [11, 22, 33]:
        return num, sums
    while num >= 10:
        num = sum(int(i) for i in str(num))
        sums.append(num)
    return num, sums

def format_solution(add):
    reduced = []
    for i in range(len(add)-1):
        current = add[i]
        next_val = add[i+1]
        num = "+".join(list(str(current)))
        reduced.append(f"{num} = {next_val}")
    return reduced

def get_numerology(name):

    name_vwls.clear()
    name_cons.clear()
    name_destiny.clear()

    for letter in name:
        if letter.isalpha():
            num = numerology.get(letter)
            name_destiny.append(num)
            if letter in vowels:
                name_vwls.append(num)
            elif letter in consonants:
                name_cons.append(num)

    soul_sum = sum(name_vwls)
    personality_sum = sum(name_cons)
    destiny_sum = sum(name_destiny)

    soul, soul_add = reduce(soul_sum, allow=False)
    personality, pers_add = reduce(personality_sum)
    destiny, destiny_add = reduce(destiny_sum)

    print(f"Soul Number is: {soul}")
    print(f"{'+'.join(map(str, name_vwls))} = {soul_sum}")
    for i in format_solution(soul_add):
        print(f"{i}")
    print()

    print(f"Personality Number is: {personality} {personality_chart.get(personality)}")
    print(f"{'+'.join(map(str, name_cons))} = {personality_sum}")
    for i in format_solution(pers_add):
        print(f"{i}")
    print()

    print(f"Destiny Number is: {destiny} {destiny_chart.get(destiny)}")
    print(f"{'+'.join(map(str, name_destiny))} = {destiny_sum}")
    for i in format_solution(destiny_add):
        print(f"{i}")
    print()

while True:
    name = input("Enter your name: ")
    if name.lower() == "done":
        break
    if name.strip():
        print(f"Hi {name} your name number in Numerology is\n")
        name = name.lower()
        get_numerology(name)
    else:
        print("Please enter a valid name.")
