def calculate_love_score(name1, name2):
    name = name1 + name2

    t = name.lower().count("t")
    r = name.lower().count("r")
    u = name.lower().count("u")
    e = name.lower().count("e")
    true = t + r + u + e
    l = name.lower().count("l")
    o = name.lower().count("o")
    v = name.lower().count("v")
    love = l + o + v + e

    print(f"T occurs {t} times")
    print(f"R occurs {r} times")
    print(f"U occurs {u} times")
    print(f"E occurs {e} times")
    print(f"Total: {true}")
    print(f"L occurs {l} times")
    print(f"O occurs {o} times")
    print(f"V occurs {v} times")
    print(f"E occurs {e} times")
    print(f"Total: {love}")

    love_count = str(true) + str(love)
    return love_count

name1 = input("Enter Name 1: ")
name2 = input("Enter Name 2: ")
print(f"Love Count: {calculate_love_score(name1, name2)}")


