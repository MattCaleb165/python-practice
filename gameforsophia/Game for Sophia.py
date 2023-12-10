#Game for Sophia
from typescript import typingPrint, typingInput
from clearscreen import clearScreen
import random
import time

clearScreen()
typingPrint("Welcome to the game.\n")
playerName = typingInput("What is your name: ")
clearScreen()
while len(playerName) != 'Sophia':
    if playerName.casefold() == "sophia":
        typingPrint("So you say that you're " + playerName + ", but you'll have to prove it first before I let you play the game.\n" )
        time.sleep(2)
        break
    else:
        typingPrint("This game is only for Sophia.\n")
        exit()

#list of possible questions
def question1():
    color = typingInput("If you're really "+ playerName + ", what has been your favorite color when you were a (little) kid? ")
    clearScreen()
    if color.casefold() == ("lime green" or "limegreen" or "lime-green"):
        typingPrint("Gah! That one was WAY too easy. Let's try a different one.\n")
        time.sleep(2)
        clearScreen()
    else:
        typingPrint("Ha! I got you! You're not Sophia. You don't get to play her game. Tsk Tsk.\n")
        exit()

def question2():
    bdayMonth = typingInput("What month were you born? ")
    clearScreen()
    if bdayMonth.casefold() == ("january"):
        typingPrint("Alright, alright, that was super easy. Don't get a big head about yourself. Let's try another.\n")
        time.sleep(2)
        clearScreen()
    else:
        typingPrint("WRONG! Gotcha. Don't try to play this game unless you're Sophia!\n")
        exit()

def question3():
    oldHouse = typingInput("What was the name of the last house you stayed in while single? ")
    clearScreen()
    if oldHouse.casefold() == ("waterlicker" or "the waterlicker" or "the waterlicker house" or "the waterlick house"):
        typingPrint("That's right! But let's try something more difficult.\n")
        time.sleep(2)
        clearScreen()
    else:
        print("Nope.")
        exit()

def question4():
    parentHome = typingInput("Fill in the blank. House on Lake _________. ")
    clearScreen()
    if parentHome.casefold() == ("drummond"):
        typingPrint("Correct! You must actually be Sophia!")
        time.sleep(2)
        clearScreen()
    else:
        typingPrint("That's not it. You can't be Sophia!")
        exit()

questionList = [question1, question2, question3]

random.choice(questionList)()
question4()
time.sleep(5)

typingPrint(r"""
  _________             .__    .__    /\            ________                      
 /   _____/ ____ ______ |  |__ |__|___)/   ______  /  _____/_____    _____   ____          
 \_____  \ /  _ \\____ \|  |  \|  \__  \  /  ___/ /   \  ___\__  \  /     \_/ __ \          
 /        (  <_> )  |_> >   Y  \  |/ __ \_\___ \  \    \_\  \/ __ \|  Y Y  \  ___/          
/_______  /\____/|   __/|___|  /__(____  /____  >  \______  (____  /__|_|  /\___  >         
        \/       |__|        \/        \/     \/          \/     \/      \/     \/ 
        
""")


