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
#Other Functions
def printspam():
    for i in range(0,25):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#Data
print("Loading[||  ]Data")
player=0
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
        rounds=15
        h1=sorted(h1)
        h2=sorted(h2)
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
        rounds=12
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
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
        rounds=10
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
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
        rounds=9
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        h5=sorted(h5)
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
        rounds=8
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        h5=sorted(h5)
        h6=sorted(h6)
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
        for i in range(0,7):
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
        rounds=7
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        h5=sorted(h5)
        h6=sorted(h6)
        h7=sorted(h7)
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
        for i in range(0,6):
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
        rounds=6
        h1=sorted(h1)
        h2=sorted(h2)
        h3=sorted(h3)
        h4=sorted(h4)
        h5=sorted(h5)
        h6=sorted(h6)
        h7=sorted(h7)
        h8=sorted(h8)
    print("Play starts with P1.")
    roundnum=0
    for i in range(0,rounds):
        roundnum+=1
        print("-----[Round "+str(roundnum)+"]-----")
        playerturn=1
        sleep(2)
        for x in range(0, players): 
            for i in range(0, 8):
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")        
            print("It's P"+str(playerturn)+"'s turn!")
            input("Pass to P"+str(playerturn)+", then press ENTER")
            goodcard=False
            playerhand=locals()["h"+str(playerturn)]
            playerkeep=globals()["p"+str(playerturn)]
            while goodcard==False:
                print("Your cards are: "+str(playerhand))
                try:
                    choosecard=int(float(input("What card do you want to keep?")))
                except:
                    print("Oops! Thats not a valid card...")
                    continue
                if choosecard in playerhand:
                    print("Taking the "+str(choosecard))
                    playerkeep[choosecard]+=1
                    playerhand.remove(choosecard)
                    goodcard=True
                else:
                    print("Oops! Thats not a valid card...")
            playerturn+=1
        if players == 2:
            h1, h2 = h2, h1
        elif players == 3:
            h1, h2, h3 = h2, h3, h1
        elif players == 4:
            h1, h2, h3, h4 = h2, h3, h4, h1
        elif players == 5:
            h1, h2, h3, h4, h5 = h2, h3, h4, h5, h1
        elif players == 6:
            h1, h2, h3, h4, h5, h6 = h2, h3, h4, h5, h6, h1
        elif players == 7:
            h1, h2, h3, h4, h5, h6, h7 = h2, h3, h4, h5, h6, h7, h1
        elif players == 8:
            h1, h2, h3, h4, h5, h6, h7, h8 = h2, h3, h4, h5, h6, h7, h8, h1
        print("GAME COMPLETE")
        print("Scoring...")
        
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
            player=playercount
            print("The player count has been set to "+str(player)+".")
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
                player=playercount
                print("The player count has been set to "+str(player)+".")
                chooseplayers=True
            else:
                print("Oops! This game can only support 2-8 players.")
    #Start Game
    elif menuchoice == 2:
        game(player)
