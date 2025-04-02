import random

print(r'''                                                                   
                                                                   
             ,---,                                                 
           ,--.' |                                                 
           |  |  :                                ,---,            
  .--.--.  :  :  :                            ,-+-. /  |           
 /  /    ' :  |  |,--.  ,--.--.        .--,  ,--.'|'   |   ,---.   
|  :  /`./ |  :  '   | /       \     /_ ./| |   |  ,"' |  /     \  
|  :  ;_   |  |   /' :.--.  .-. | , ' , ' : |   | /  | | /    /  | 
 \  \    `.'  :  | | | \__\/: . ./___/ \: | |   | |  | |.    ' / | 
  `----.   \  |  ' | : ," .--.; | .  \  ' | |   | |  |/ '   ;   /| 
 /  /`--'  /  :  :_:,'/  /  ,.  |  \  ;   : |   | |--'  '   |  / | 
'--'.     /|  | ,'   ;  :   .'   \  \  \  ; |   |/      |   :    | 
  `--'---' `--''     |  ,     .-./   :  \  \'---'        \   \  /  
                      `--`---'        \  ' ;              `----'   
                                       `--`                        ''')
players = {'Stephen Curry': [85, 90, 78, 74, 95, 95, 85, 98, 700],
           'Lebron James:': [90, 86, 80, 95, 86, 89, 96, 95, 717],
           'Jayson Tatum':  [84, 84, 75, 75, 84, 84, 86, 80, 652],
           'Kyrie Irving:': [85, 91, 76, 73, 96, 94, 84, 97, 696],
           'Anthony Edwards': [86, 89, 85, 80, 87, 86, 94, 80, 687],
           'Luka Doncic':   [88, 85, 86, 89, 85, 81, 90, 86, 690],
           'Kevin Durant': [89, 86, 79, 94, 82, 80, 89, 87, 686],
           'Jimmy Buttler': [87, 84, 81, 92, 83, 90, 90, 85, 692]}
stat = ["Power", "Speed", "Health", "Dunk", "Assist", "Steals", "Rebound", "Three Points", "Over All Rate"]
user_money = {}
result = 0
def random_stat():
    return random.randint(0, len(stat)-1)

while True:
    name = input("Enter your name: ")
    money = 0
    while True:
        p1, stat1 = random.choice(list(players.items()))
        p2, stat2 = random.choice(list(players.items()))
        while p1 == p2:
            p2, stat2 = random.choice(list(players.items()))
        print(f"\nPlayer 1: {p1}")
        print(f"Player 2: {p2}")

        while True:
            stat_index = random_stat()
            if stat1[stat_index] != stat2[stat_index]:
                break
            else:
                print("Draw. Comparing another Stat/Profile...")

        guess = int(input(f"Guess: Who has more {stat[stat_index]}?\n"
                          f"Type 1 or 2: "))
        while True:
            if stat1[stat_index] > stat2[stat_index]:
                result = 1
                break
            else:
                result = 2
                break

        if result == guess:
            money += 1000
            print(f"Result: Correct Guess \n"
                  f"Money earned: ${money}")
            continue

        else:
            print(f"Result: Incorrect Guess!\n"
                  f"Total Money Earned: ${money}")
            break

    user_money[name] = money
    play_again = input("Do you want to play again? ").lower()
    if play_again != "yes":
        print("\nGame Over! Here are the final scores:")
        sorted_scores = sorted(user_money.items(), key=lambda x: x[1], reverse=True)
        for player, earnings in sorted_scores:
            print(f"{player}: ${earnings}")
        break




