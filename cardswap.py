"""
CardSwap Program
CardSwap Game: https://cardswap.github.io/game
Coded by EpicPuppy613
.exe built by pyinstaller(https://www.pyinstaller.org/)
"""
#Imports
import random as r
#Data
players=0
#Cards
cards={1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
p1={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p2={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p3={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p4={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p5={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p6={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p7={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
p8={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
h1={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
h2={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
h3={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
h4={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
h5={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
h6={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
h7={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
h8={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0}
#Main Loop
while True:
    mainmenu=False
    print("""Welcome to CardSwap!
CardSwap is a game of card drafting stragey.
During each round, players will choose a card to keep and pass the rest of their hand on.
Sidenote: Even though the original game uses a standard playing card deck,
the program simiplifies the cards into numbers(A=1, J=11...)for simplicity sake.""")
    input("[Press ENTER to Start]")
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
#Main Menu
    mainmenu=False
    while mainmenu==False:
        try:
            print("""What do you want to do?
[0]Quit
[1]Configure Game
[2]Start Game
[3]Credits
[4]Original Game""")
            menuchoice=int(float(input(">")))
        except:
            print("Oops! Thats not a valid choice...")
            continue
        if menuchoice >=0 and menuchoice <=4:
            mainmenu=True
    if menuchoice == 0:
        print("Thanks for playing!")
        input("[Press ENTER to Exit]")
        break