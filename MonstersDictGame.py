from tkinter import Tk, Label, Button, Listbox
import random

monsterDict = {}

class monster:
    def __init__(self, data):
        self.data = data
        self.id = data[0]
        self.name = data[1]
        self.origin = data[2]
        self.description = data[3]
        self.attack = data[4]
        self.mForce = data[5]
        self.mDef = data[6]
        self.pDef = data[7]
        self.int = data[8]
        self.hp = data[9]
        self.exp = data[10]

    def getData(self):
        return self.data

def setData():
    #loop to get data from list and add to dict
    with open("MonstersExtension/Monsters.txt", "r") as f:
        for lines in f:
            temp = lines.strip("\n")
            temp = lines.split(",")
            monsterDict[temp[1]] = monster(temp)

######################################################
# Main
######################################################
setData()
attr = ['attack', 'mForce', 'mDef', 'pDef', 'int', 'hp']
player1 = []
player2 = []

def makecards():
    cards = list(monsterDict.items())
    for i in range(5):
        random.shuffle(cards)
        player1.append(cards.pop()[1])
        player2.append(cards.pop()[1])

def pick(player):
    chosen = int(input(f"Player {player} Please choose an attribute, from 1 to 6"))
    return (attr[chosen-1])
    
def printcards():
    print("""
    
    -------------
    
    """)
    print(f"Player 1 has {len(player1)} cards left")
    print(f"Player 2 has {len(player2)} cards left")
    print("Player 1's card is: ")
    print(player1[0].name)
    for i in range(1, 7):
        print(attr[i - 1]+ ":" + player1[0].getData()[i + 3])

    print(""""
    
    -------------
    
    """)
    print("Player 2's card is: ")
    print(player2[0].name)
    for i in range(1, 7):
        print(attr[i - 1]+ ":" + player2[0].getData()[i + 3])


    ##print player 1 + 2 card

def compare(stat):
    statIndex = attr.index(stat)
        
    p1 = int(player1[0].getData()[statIndex + 4])
    p2 = int(player2[0].getData()[statIndex + 4])
    if p1 > p2:
        return 1
    elif p2 > p1:
        return 2
    else:
        return 0    ## for draw

def trade(winner):
    if winner == 0:
        return None
    elif winner == 1:
        temp = player1[0]
        player1.remove(temp)
        player1.append(temp)
        temp2 = player2[0]
        player2.remove(temp2)
        player1.append(temp2)
    elif winner == 2:
        temp = player2[0]
        player2.remove(temp)
        player2.append(temp)
        temp2 = player1[0]
        player1.remove(temp2)
        player2.append(temp2)
        
    print("""
    
    --------------
    
    """)
    print(f"Player {winner} won this round")
    print("""
    
    --------------
    
    """)

def main():
    ##turns
    makecards()
    while (len(player1) > 0) and (len(player2) > 0):
        playerturn = random.randint(1, 2)
        print(f"it's player {playerturn}\'s turn")
        printcards()
        winner = compare(pick(playerturn))
        trade(winner)
        if playerturn == 1:
            playerturn = 2
        else:
            playerturn = 1
    print(f"Player {winner} won!")

main()
