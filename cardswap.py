"""
CardSwap Program
CardSwap Game: https://cardswap.github.io/game
Coded by EpicPuppy613
.exe built by pyinstaller(https://www.pyinstaller.org/)
"""
print("Please wait, loading")
#Imports
print("Loading[|   ]Libraries")
import random as r
import time as t
t.sleep(0.5)
#Data
print("Loading[||  ]Data")
players=0
t.sleep(0.5)
#Cards
print("Loading[||| ]Cards")
cards={1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
p1={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p2={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p3={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p4={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p5={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p6={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p7={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p8={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0} 
t.sleep(0.5)
#Define Game
print("Loading[||||]Game")
def game(players):
    print(str(players))
    #Deal Cards
    if players == 2:
        h1=[]
        h2=[]
        cardbank=[]
        for x in range(1,14):
            for z in range(0,cards[x]):
                cardbank.append(x)
        for i in range(0,15):
            cardadd=r.choice(cardbank)
            h1.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h2.append(cardadd)
            cardbank.remove(cardadd)
        h1=sorted(h1)
        h2=sorted(h2)
        print(h1)
        print(h2)
        print(cardbank)
    elif players == 3:
        h1=[]
        h2=[]
        h3=[]
        cardbank=[]
        for x in range(1,14):
            for z in range(0,cards[x]):
                cardbank.append(x)
        for i in range(0,12):
            cardadd=r.choice(cardbank)
            h1.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h2.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h3.append(cardadd)
            cardbank.remove(cardadd)
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        print(h1)
        print(h2)
        print(h3)
        print(cardbank)
    elif players == 4:
        h1=[]
        h2=[]
        h3=[]
        h4=[]
        cardbank=[]
        for x in range(1,14):
            for z in range(0,cards[x]):
                cardbank.append(x)
        for i in range(0,10):
            cardadd=r.choice(cardbank)
            h1.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h2.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h3.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h4.append(cardadd)
            cardbank.remove(cardadd)
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        print(h1)
        print(h2)
        print(h3)
        print(h4)
        print(cardbank)
    elif players == 5:
        h1=[]
        h2=[]
        h3=[]
        h4=[]
        h5=[]
        cardbank=[]
        for x in range(1,14):
            for z in range(0,cards[x]):
                cardbank.append(x)
        for i in range(0,9):
            cardadd=r.choice(cardbank)
            h1.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h2.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h3.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h4.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h5.append(cardadd)
            cardbank.remove(cardadd)
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        h5=sorted(h5)
        print(h1)
        print(h2)
        print(h3)
        print(h4)
        print(h5)
        print(cardbank)
    elif players == 6:
        h1=[]
        h2=[]
        h3=[]
        h4=[]
        h5=[]
        h6=[]
        cardbank=[]
        for x in range(1,14):
            for z in range(0,cards[x]):
                cardbank.append(x)
        for i in range(0,8):
            cardadd=r.choice(cardbank)
            h1.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h2.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h3.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h4.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h5.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h6.append(cardadd)
            cardbank.remove(cardadd)
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        h5=sorted(h5)
        h6=sorted(h6)
        print(h1)
        print(h2)
        print(h3)
        print(h4)
        print(h5)
        print(h6)
        print(cardbank)
    elif players == 7:
        h1=[]
        h2=[]
        h3=[]
        h4=[]
        h5=[]
        h6=[]
        h7=[]
        cardbank=[]
        for x in range(1,14):
            for z in range(0,cards[x]):
                cardbank.append(x)
        for i in range(0,8):
            cardadd=r.choice(cardbank)
            h1.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h2.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h3.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h4.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h5.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h6.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h7.append(cardadd)
            cardbank.remove(cardadd)
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        h5=sorted(h5)
        h6=sorted(h6)
        h7=sorted(h7)
        print(h1)
        print(h2)
        print(h3)
        print(h4)
        print(h5)
        print(h6)
        print(h7)
        print(cardbank)
    elif players == 8:
        h1=[]
        h2=[]
        h3=[]
        h4=[]
        h5=[]
        h6=[]
        h7=[]
        h8=[]
        cardbank=[]
        for x in range(1,14):
            for z in range(0,cards[x]):
                cardbank.append(x)
        for i in range(0,8):
            cardadd=r.choice(cardbank)
            h1.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h2.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h3.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h4.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h5.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h6.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h7.append(cardadd)
            cardbank.remove(cardadd)
            cardadd=r.choice(cardbank)
            h8.append(cardadd)
            cardbank.remove(cardadd)
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        h5=sorted(h5)
        h6=sorted(h6)
        h7=sorted(h7)
        h8=sorted(h8)
        print(h1)
        print(h2)
        print(h3)
        print(h4)
        print(h5)
        print(h6)
        print(h7)
        print(h8)
        print(cardbank)
t.sleep(1)
#Main Loop
print("Loading Complete!")
print("""Welcome to CardSwap!
CardSwap is a game of card drafting stragey.
During each round, players will choose a card to keep and pass the rest of their hand on.
Sidenote: Even though the original game uses a standard playing card deck,
the program simiplifies the cards into numbers(A=1, J=11...)for simplicity sake.""")
input("[Press ENTER to Start]")
while True:
    mainmenu=False
#Player Choice
    chooseplayers=False
    while chooseplayers==False:
        try:
            playercount=int(float(input("How many players are playing?\n>")))
        except:
            print("Oops! That's not a valid number...")
            continue
        if playercount >=2 and playercount <=8:
            players=playercount
            print("The player count has been set to "+str(players)+".")
            chooseplayers=True
        else:
            print("Oops! This game can only support 2-8 players.")
#Main Menu
    mainmenu=False
    while mainmenu==False:
        try:
            print("""What do you want to do?
[0]Quit
[1]Change Players
[2]Start Game
[3]Credits
[4]Original Game""")
            menuchoice=int(float(input(">")))
        except:
            print("Oops! Thats not a valid choice...")
            continue
        if menuchoice >=0 and menuchoice <=4:
            mainmenu=True
    #Quit
    if menuchoice == 0:
        print("Thanks for playing!")
        input("[Press ENTER to Exit]")
        break
    #Change Players
    elif menuchoice == 1:
        chooseplayers=False
        while chooseplayers==False:
            try:
                playercount=int(float(input("How many players are playing?\n>")))
            except:
                print("Oops! That's not a valid number...")
                continue
            if playercount >=2 and playercount <=8:
                players=playercount
                print("The player count has been set to "+str(players)+".")
                chooseplayers=True
            else:
                print("Oops! This game can only support 2-8 players.")
    #Start Game
    elif menuchoice == 2:
        game(players)
