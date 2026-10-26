import random

money = 10

def roulette():
    con = False
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
        money += chips * 2
        print(f"Congrats! Your new balance is {money}!")
    elif color.lower() == wincolor and wincolor == "green" and color.lower() == "green":
        money += chips * 10
        print(f"Congrats! Your new balance is {money}!")
    else:
        money = money - chips
        print(f"You lost, your new balance is {money}.")

roulette()