bids = {}
print('''88888b.d88b.  .d88b. 88888b.  .d88b. 888  888 
888 "888 "88bd88""88b888 "88bd8P  Y8b888  888 
888  888  888888  888888  88888888888888  888 
888  888  888Y88..88P888  888Y8b.    Y88b 888 
888  888  888 "Y88P" 888  888 "Y8888  "Y88888 
                                          888 
                                     Y8b d88P 
                                      "Y88P"  \n\n''')

while True:
    amount = 0
    bidder = ''
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid

    bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if bidders == "yes":
        print("\n" * 5)
        continue
    else:
        for x, y in bids.items():
            if y > amount:
                amount = y
                bidder = x
        print(f"The winner is {bidder} with a bid of ${amount}")
        break




