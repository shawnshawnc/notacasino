import random

money = 10
broke = False
con = False
deck = [
    {
        "class" : "diamond",
        "value" : "3",
        "21value" : 3
    },
    {
        "class" : "clubs",
        "value" : "3",
        "21value" : 3
    },
    {
        "class" : "hearts",
        "value" : "3",
        "21value" : 3
    },
    {
        "class" : "spades",
        "value" : "3",
        "21value" : 3
    },
    {
        "class" : "diamond",
        "value" : "4",
        "21value" : 4
    },
    {
        "class" : "clubs",
        "value" : "4",
        "21value" : 4
    },
    {
        "class" : "hearts",
        "value" : "4",
        "21value" : 4
    },
    {
        "class" : "spades",
        "value" : "4",
        "21value" : 4
    },
    {
        "class" : "diamond",
        "value" : "5",
        "21value" : 5
    },
    {
        "class" : "clubs",
        "value" : "5",
        "21value" : 5
    },
    {
        "class" : "hearts",
        "value" : "5",
        "21value" : 5
    },
    {
        "class" : "spades",
        "value" : "5",
        "21value" : 5
    },
    {
        "class" : "diamond",
        "value" : "6",
        "21value" : 6
    },
    {
        "class" : "clubs",
        "value" : "6",
        "21value" : 6
    },
    {
        "class" : "hearts",
        "value" : "6",
        "21value" : 6
    },
    {
        "class" : "spades",
        "value" : "6",
        "21value" : 6
    },
    {
        "class" : "diamond",
        "value" : "7",
        "21value" : 7
    },
    {
        "class" : "clubs",
        "value" : "7",
        "21value" : 7
    },
    {
        "class" : "hearts",
        "value" : "7",
        "21value" : 7
    },
    {
        "class" : "spades",
        "value" : "7",
        "21value" : 7
    },
    {
        "class" : "diamond",
        "value" : "8",
        "21value" : 8
    },
    {
        "class" : "clubs",
        "value" : "8",
        "21value" : 8
    },
    {
        "class" : "hearts",
        "value" : "8",
        "21value" : 8
    },
    {
        "class" : "spades",
        "value" : "8",
        "21value" : 8
    },
    {
        "class" : "diamond",
        "value" : "9",
        "21value" : 9
    },
    {
        "class" : "clubs",
        "value" : "9",
        "21value" : 9
    },
    {
        "class" : "hearts",
        "value" : "9",
        "21value" : 9
    },
    {
        "class" : "spades",
        "value" : "9",
        "21value" : 9
    },
    {
        "class" : "diamond",
        "value" : "10",
        "21value" : 10
    },
    {
        "class" : "clubs",
        "value" : "10",
        "21value" : 10
    },
    {
        "class" : "hearts",
        "value" : "10",
        "21value" : 10
    },
    {
        "class" : "spades",
        "value" : "10",
        "21value" : 10
    },
    {
        "class" : "diamond",
        "value" : "Jack",
        "21value" : 10
    },
    {
        "class" : "clubs",
        "value" : "Jack",
        "21value" : 10
    },
    {
        "class" : "hearts",
        "value" : "Jack",
        "21value" : 10
    },
    {
        "class" : "spades",
        "value" : "Jack",
        "21value" : 10
    },
    {
        "class" : "diamond",
        "value" : "Queen",
        "21value" : 10
    },
    {
        "class" : "clubs",
        "value" : "Queen",
        "21value" : 10
    },
    {
        "class" : "hearts",
        "value" : "Queen",
        "21value" : 10
    },
    {
        "class" : "spades",
        "value" : "Queen",
        "21value" : 10
    },
    {
        "class" : "diamond",
        "value" : "King",
        "21value" : 10
    },
    {
        "class" : "clubs",
        "value" : "King",
        "21value" : 10
    },
    {
        "class" : "hearts",
        "value" : "King",
        "21value" : 10
    },
    {
        "class" : "spades",
        "value" : "King",
        "21value" : 10
    },
    {
        "class" : "diamond",
        "value" : "Ace",
        "21value" : 1
    },
    {
        "class" : "clubs",
        "value" : "Ace",
        "21value" : 1
    },
    {
        "class" : "hearts",
        "value" : "Ace",
        "21value" : 1
    },
    {
        "class" : "spades",
        "value" : "Ace",
        "21value" : 1
    },
    {
        "class" : "diamond",
        "value" : "2",
        "21value" : 2
    },
    {
        "class" : "clubs",
        "value" : "2",
        "21value" : 2
    },
    {
        "class" : "hearts",
        "value" : "2",
        "21value" : 2
    },
    {
        "class" : "spades",
        "value" : "2",
        "21value" : 2
    }
]

def bankrupt():
    global money
    global broke
    if money <= 0:
        print("You are broke. Game Over.")
        broke = True

def roulette():
    global con
    global money
    chips = int(input(f"How much money would you like to bet? You have ${money} : "))

    winnum = random.randint(0,36)

    if winnum >=0 and winnum <= 17:
        wincolor = "black"
    
    if winnum >= 18 and winnum <= 34:
        wincolor = "red"
    
    if winnum == 35 or winnum == 36:
        wincolor = "green"
    
    while con == False:
        if chips > 0 and chips <= money:
            color = input("Black, Red, or Green? : ")
            con = True
        else:
            chips = int(input(f"You do not have that much money, how much money would you like to bet? You have ${money} : "))
    print(f"The ball landed on {wincolor}.")

    if color.lower() == wincolor:
        money += chips
        print(f"Congrats! Your new balance is {money}!")
    elif color.lower() == wincolor and wincolor == "green" and color.lower() == "green":
        money += chips * 10
        print(f"Congrats! Your new balance is {money}!")
    else:
        money = money - chips
        print(f"You lost, your new balance is {money}.")
        con = False

def gencard():
    card = random.choice(deck)
    return card

def blackjack():
    global money
    global con
    dealer = 0
    player = 0
    card = ""
    action = ""
    dealerbust = False
    playerbust = False
    playerwin = False
    dealerwin = False
    tie = False
    playerdeck = []
    dealerdeck = []
    dealerdeckplayer = []
    chips = int(input(f"How much money would you like to bet? You have ${money}. "))
    while con == False:
            if chips > 0 and chips <= money:
                con = True
            else:
                chips = int(input(f"You do not have that much money, how much money would you like to bet? You have ${money} : "))
    
    while dealerbust == False and tie == False and playerbust == False: 
        #card generating
        while dealer <= 17 or dealer <= 21 and dealerbust == False:
            card = gencard()
            dealer += int(card["21value"])
            dealerdeck.append(f"{card["value"]} of {card["class"]}")
            dealerdeckplayer.append(f"{card["value"]} of {card["class"]}")
            if dealer > 21:
                dealerbust == False
        if dealer == 21:
            dealerwin = True
        dealerdeckplayer.pop(1)
        dealerdeckplayer.append("? Card")
        #--------------------------------------------------------

        print(f"The dealer's deck is {dealerdeckplayer[0]}, {dealerdeckplayer[1]}")

        for i in range(2):
            card = gencard()
            player += int(card["21value"])
            playerdeck.append(f"{card["value"]} of {card["class"]}")
            if player == 21:
                playerwin = True
                break
        
        while action != "stand" and playerbust == False:
            print(f"Your deck is {playerdeck} and the value is {player}.")
            action = input("Would you like to hit or stand? ")
            if action.lower() == "hit":
                card = gencard()
                player += int(card["21value"])
                playerdeck.append(f"{card["value"]} of {card["class"]}")
            if player > 21:
                playerbust = True
                break
            if action.lower() == "stand":
                action = "stand"
                break
            else:
                print("error L371")

        if dealer == player:
            tie = True

    if dealerbust == True or playerwin == True:
        print(f"Congrats! You won {chips}!")
        money += chips
        print(f"Your new balance is {money}.")
    if playerbust == True or dealerwin == True:
        print(f"You lost.")
        money -= chips
        print(f"Your new balance is {money}.")
    if tie == True:
        print("It was a tie!")
        print(f"Your balance is {money}.")
        
        
        

    
blackjack()