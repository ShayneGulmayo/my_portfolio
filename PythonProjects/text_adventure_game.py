print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island\n"
      "Your mission is to find the treasure.")
l_or_r = input("You're at a crossroad, where do you want to go? Type \"left\" or \"right\".\n").lower()

if l_or_r == 'left':
    s_or_w = input("You've come to a lake. There is an island in the middle of the lake. "
                   "Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if s_or_w == 'wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors."
                     "One red, one yellow, and one blue. Which color would you choose?\n").lower()
        if door == 'yellow':
            print("You found the treasure. You Win!")
        elif door == 'blue':
            print("You got eaten by beasts. Game Over.")
        elif door == 'red':
            print("You got burned by fire. Game Over.")
        else:
            print("Game Over.")
    else:
        print("You got attacked by trout. Game Over")
else:
    print("You fell into a hole! GAME OVER.")

