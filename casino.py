import random
import os
import time
con = False
money = 10
broke = False
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
        while dealer <= 17:
            card = gencard()
            dealer += int(card["21value"])
            dealerdeck.append(f"{card["value"]} of {card["class"]}")
            dealerdeckplayer.append(f"{card["value"]} of {card["class"]}")
            if dealer > 21:
                dealerbust = True
                
        if dealer == 21:
            dealerwin = True
            break
        dealerdeckplayer.pop(1)
        dealerdeckplayer.append("? Card")

        #--------------------------------------------------------


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

        if dealer == player:
            tie = True

    if dealerbust == True or playerwin == True:
        print(f"Congrats! You won ${chips}!")
        money += chips
        print(f"Your new balance is {money}.")
    elif playerbust == True or dealerwin == True:
        print(f"You lost.")
        money -= chips
        print(f"Your new balance is ${money}.")
    elif tie == True:
        print("It was a tie!")
        print(f"Your balance is ${money}.")
        
def coinflip():
    global con
    global money
    coin = ["heads", "tails"]
    winflip = random.choice(coin)
    chips = int(input(f"How much money would you like to bet? You have ${money} : "))
    while con == False:
            if chips > 0 and chips <= money:
                bet = input("Heads or Tails? ")
                con = True
            else:
                chips = int(input(f"You do not have that much money, how much money would you like to bet? You have ${money} : "))
    print(f"The coin landed on {winflip}!")
    if winflip == bet.lower():
        print("Congrats you won!")
        money += chips
    else:
        print("You lost.")
        money -= chips

def slots():
    global money
    global con
    symbols = ["7️⃣", "💰", "👑", "🌟", "🍒", "🔑", "💎", "👍", "🌈", "🎪", "🎰", "🦴", "💲", "🪙", "🤌", "🧭", "👟", "🗿", "📢", "🎹"]
    symbol1 = random.choice(symbols)
    symbol2 = random.choice(symbols)
    symbol3 = random.choice(symbols)
    print("The price to play is $5, the Jack Pot is $500,000.")
    chips = 5
    while con == False:
            if chips <= 5 and money >= chips:
                con == True
                break
            else:
                print("You do not have enough money to play this game.")
                break
    print(f"You rolled: {symbol1} {symbol2} {symbol3}")
    if symbol1 == symbol2 == symbol3:
        print("Congrats! You got $500,000!")
        money += 500000
    else:
        print("You did not win.")
        money -= 5
    print(f"Your new balance is ${money}.")

def cardguess():
    global money
    global con
    card = []
    state = ""
    card.append(gencard())
    chips = int(input(f"How much money would you like to bet? You have ${money} : "))
    while con == False:
        if chips > 0 and chips <= money:
            bet = input("Will the card be odd, even, or a face card? ")
            con = True
        else:
            chips = int(input(f"You do not have that much money, how much money would you like to bet? You have ${money} : "))
    try:
        if int(card[0]["value"]) % 2 == 0:
            state = "even"
        elif int(card[0]["value"]) % 2 == 1:
            state = "odd"
    except:
        state = "face card"
    if bet.lower() == state:
        print(f"Congrats! The card was {card[0]["value"].title()}.")
        money += chips
    else:
        print(f"You lost! The card was {card[0]["value"].title()}.")
        money -= chips
    print(f"Your new balance is {money}.")

def redblack():
    global money
    global con
    red = 0
    black = 0
    deck = []
    playerdeck = []
    winner = ""
    
    for i in range(5):
        card = gencard()
        deck.append(card)
        playerdeck.append(f"{card["value"]} of {card["class"]}")
        
    chips = int(input(f"How much money would you like to bet? You have ${money}. "))
    while con == False:
            if chips > 0 and chips <= money:
                color = input("Will the majority of the colors be red or black? ")
                con = True
            else:
                chips = int(input(f"You do not have that much money, how much money would you like to bet? You have ${money} : "))
    
    for i in range(len(deck)):
        if deck[i]["class"] == "diamond" or deck[i]["class"] == "hearts":
            red += 1
        else:
            black += 1
    
    if red > black:
        winner = "red"
    elif red < black:
        winner = "black"
    elif red == 5:
        winner = "full sweep red"
    elif black == 5:
        winner = "full sweep black"

    if winner == color.lower():
        print(f"Congrats! You won!")
        money += chips
    elif winner == f"full sweep {color.lower()}":
        print(f"Congrats!! You won big!!!!")
        money += chips*2
    else:
        print("You lost.")
        money -= chips
    
    print(f"The deck was {playerdeck}.")
    print(f"Your new balance is {money}.")

def casino():
    global money
    global bankrupt
    global con
    print("Your in debt")
    time.sleep(2)
    print("They are coming for you mijo")
    time.sleep(2)
    print("You need to make 10000 habibi")
    time.sleep(2)
    print("Hit the casino... RUN MIJO")
    time.sleep(5)
    os.system('cls')
    while money < 10000:
        print(f"You have to pay off {10000-money}.")
        game = int(input("What game would you like to play? 0: Roulette 1: Blackjack 2: Coin Flip 3: Slots 4: Card Guess 5: Red or Black "))
        if game == 0:
            roulette()
        if game == 1:
            blackjack()
        if game == 2:
            coinflip()
        if game == 3:
            slots()
        if game == 4:
            cardguess()
        if game == 5:
            redblack()
        bankrupt()
        if broke == True:
            time.sleep(5)
            os.system('cls')
            print("You lost all your money.")
            print("Game Over")
            time.sleep(10)
            break
        con = False
        time.sleep(10)
        os.system('cls')
    os.system('cls')
    if broke == True:
        print("")
    else:
        print("You paid off all your debt.")
        print("You got slimed anyway.")


casino()