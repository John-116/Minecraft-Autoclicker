# Adjustable Mineacraft Autoclicker
import sys
from time import sleep
from pyautogui import click
import keyboard


# Define Possible tools and materials
tools = ["trident", "pickaxe", "axe", "sword", "shovel", "hoe", "fists"]
materials = ["wood", "stone", "iron", "gold", "diamond", "netherite"]

print("Adjustable Minecraft Autoclicker")

def main():
    
    # Get Tool
    tool = input("What weapon are you using? (Axe, Sword, etc.) ")
    tool= tool.lower()
    
    # Ensure that there is a valid tool
    if tool not in tools:
        print("Invalid Tool \nValid Tools are: Trident, Pickaxe, Axe, Sword, Shovel, Hoe, Fists")
        main()
    
    # Tool sorting
    if tool == "trident": trident()

    if tool == "pickaxe": pickaxe()

    if tool == "axe": axe()

    if tool == "sword": sword()

    if tool == "shovel" or tool == "hoe": hoeShovel()

    if tool == "fists" or tool == "fist": fist()

# Trident Functino
def trident():
    startWarning()

    while True:
        if keyboard.is_pressed('Y'):
            sys.exit("Program Exited! Y pressed!")
        click()
        sleep(0.9)

# Pickaxe Function
def pickaxe():
    startWarning()
    
    while True:
        if keyboard.is_pressed('Y'):
            sys.exit("Program Exited! Y pressed!")
        click()
        sleep(0.8)

# Axe Function
def axe():
    # Get the axe's material
    axematerial = input("What is your axe made of? ")
    axematerial = axematerial.lower()

    if axematerial not in materials:
        print("Invalid material! Valid materials are: Wood, Stone, Iron, Gold, Diamond, Netherite")
        axe()
    
    startWarning()

    # Wood and stone axes
    if axematerial == "wood" or axematerial == "stone":
        while True:
            if keyboard.is_pressed('Y'):
                sys.exit("Program Exited! Y pressed!")
            click()
            sleep(1.2)
    
    # Iron axe
    if axematerial == "iron":
        while True:
            if keyboard.is_pressed('Y'):
                sys.exit("Program Exited! Y pressed!")
            click()
            sleep(1.1)

    # Gold, Diamond or Netherite axes
    else:
        while True:
            if keyboard.is_pressed('Y'):
                sys.exit("Program Exited! Y pressed!")
            click()
            sleep(1)

# Sword Function
def sword():
    startWarning()
    
    while True:
        if keyboard.is_pressed('Y'):
            sys.exit("Program Exited! Y pressed!")
        click()
        sleep(0.6)

# Hoe and Shovel Function
def hoeShovel():
    startWarning()

    while True:
            if keyboard.is_pressed('Y'):
                sys.exit("Program Exited! Y pressed!")
            click()
            sleep(1)

# Fist Function
def fist():
    startWarning()

    while True:
        if keyboard.is_pressed('Y'):
            sys.exit("Program Exited! Y pressed!")
        click()
        sleep(0.25)

# Warning that the program will begin
def startWarning():
    print("Hold Y to exit the autoclicker! Autoclicking will begin in 5 seconds")
    sleep(5)

main()
