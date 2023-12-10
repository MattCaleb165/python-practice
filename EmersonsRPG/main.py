import math
import pyglet, sys, os
from typescript import typingPrint, typingInput
from clearscreen import clearScreen
from rolldice import six_side
import random
import time

character = {}

clearScreen()
typingPrint("Welcome to Caleb's Monty Python and the Holy Snail game.\n")

while True:
    character["playerGender"] = typingInput("Will your character be male or female: ")
    if character["playerGender"] == ("m" or "male"):
        clearScreen()
        genderRef = "Mr."
        pronoun1 = "his"
        typingPrint("You selected male. \n\n")
        break
    elif character["playerGender"] == ("f" or "female"):
        clearScreen()
        genderRef = "Mrs."
        pronoun1 = "her"
        typingPrint("You selected female. \n\n")
        break
    else:
        clearScreen()
        typingPrint("Invalid. There are only two genders in this game. Male or Female (m or f). Try again or rage quit.\n\n")

while True:
    character["playerFirst"] = typingInput("What is your character's first name: ")
    if len(character["playerFirst"]) > 0 and character["playerFirst"].isalpha():
        clearScreen()
        typingPrint(character["playerFirst"] + "! A very good name for a character.\n\n")
        break
    elif len(character["playerFirst"]) < 1:
        clearScreen()
        typingPrint("No entry, try again.\n\n")
        time.sleep(2)
        clearScreen()
    elif not character["playerFirst"].isalpha():
        clearScreen()
        typingPrint("That's not a word.. at least, not one I can read! Try again.\n\n")
        time.sleep(2)
        clearScreen()

while True:
    character["playerLast"] = typingInput("What is " + character["playerFirst"] + "'s last name: ")
    if len(character["playerLast"]) > 0 and character["playerLast"].isalpha():
        clearScreen()
        typingPrint(character["playerFirst"] + " " + character["playerLast"] + ". Tis a noble sounding name.\n\n")
        break
    elif len(character["playerLast"]) < 1:
        clearScreen()
        typingPrint("No entry, try again.\n\n")
        time.sleep(2)
        clearScreen()
    elif not character["playerLast"].isalpha():
        clearScreen()
        typingPrint("That's not a word.. at least, not one I can read! Try again.\n\n")
        time.sleep(2)
        clearScreen()

while True:
    character["playerAge"] = typingInput("How old is " + character["playerFirst"] + " " + character["playerLast"] + "? ")
    if int(character["playerAge"]) >= 18 and int(character["playerAge"]) <= 50:
        clearScreen()
        typingPrint(character["playerFirst"] + " " + character["playerLast"] + " is the ripe age of " + character["playerAge"] + " years old.\n\n")
        time.sleep(2)
        clearScreen()
        break
    elif int(character["playerAge"]) > 0 and int(character["playerAge"]) < 18:
        clearScreen()
        typingPrint("Are you sure that " + character["playerFirst"] + " " + character["playerLast"] + " is old enough to go on an adventure? " + character["playerAge"] + " years old would usually require an adult's permission.\n\n")
        time.sleep(2)
        clearScreen()
        break
    elif int(character["playerAge"]) > 50 and int(character["playerAge"]) <= 80:
        clearScreen()
        typingPrint("Wowwwww! " + genderRef + " " + character["playerLast"] + " has seen a lot of action in " + pronoun1 + " days. Perhaps it's time to consider retirement? \n\nAlas, we shall allow the adventure to commence (but only with a normal amount of bathroom breaks)! \n\n")
        time.sleep(2)
        clearScreen()
        break
    elif not character["playerAge"].isdigit():
        clearScreen()
        print("That is not a number. Try again.")
        time.sleep(2)
        clearScreen()
    elif int(character["playerAge"]) <= 0:
        clearScreen()
        print("Your player must be born already... You know that.")
        time.sleep(2)
        clearScreen()
    else:
        clearScreen()
        print("AH! Your character is too old for an adventure.")
        time.sleep(2)
        clearScreen()



character["playerHealth"] = 0
character["playerStrength"] = 0

print(character)