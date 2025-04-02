import random

print(r'''            $$ $             
             \\O//?
             $            
            $ |              
             /_\             
           _|___|_           
         _|___|___|_         
       _|___|___|___|_       
     _|___|___|___|___|_     
   _|___|___|___|___|___|_   
 _|___|___|___|___|___|___|_ 
|___|___|___|___|___|___|___|
 \o/ \o/ \o/ \o/ \o/ \o/ \o/ 
  |   |   |   |   |   |   |  
 / \ / \ / \ / \ / \ / \ / \ ''')

print("This is a Peraphy Game, You will win 1,000 each correct guess for Higher or Lower Card Number\n"
      "You will loose your money if Card is equal!\n"
      "Setup your Game Mode First\n\n")

prize = 0
num_card = int(input("Number of card you want to Play?\n"))
rand_range = int(input("Random numbers to display from 1 to ?\n"))
card = [random.randint(1,rand_range) for _ in range(num_card)]
r = 0
print(card[0])
while r < num_card-1:
    guess = input("Guess the next card if Higher or Lower use H or L\n")
    guess.lower()

    if card[r] < card[r+1]:
        correct_guess = 'h'
        h_or_l = 'Higher'
    elif card[r] > card[r+1]:
        correct_guess = 'l'
        h_or_l = 'Lower'
    else:
        correct_guess = 'e'

    r += 1
    if guess == correct_guess:
        prize += 1000
        print(card[r])
        print(f"Correct its {h_or_l} your prize is {prize}")
    elif correct_guess == 'e':
        prize = 0
        print(card[r])
        print("Card is Equal prize reset to 0")
    else:
        print(card[r])
        print(f"Wrong guess your prize remains {prize}")

    if r == num_card-1:
        print(f"Congratulations you win a total prize of {prize}")


