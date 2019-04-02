# APCS-P
# Olivia Schreiner (4-2-19)
# Choose your own adventure labyrinth game


# Imports
import random
import sys
import os
from time import sleep


# Variables
alive = True
sanity = 10
num_paths = 25
survive = False

# Access ASCII Art
def get_art(file_num):
    path = 'art'
    file_names = os.listdir(path)
    file = path + "/" + file_names[file_num]

    with open(file, 'r') as f:
        lines = f.read()
        print(lines)
    print()
    
# Start
def start_screen():
    get_art(1)

    
#Endings
def win(survive):
    if survive:
        get_art(2)
        type_text("You escaped the labyrinth and will live to see another day.")
        
def go_crazy(sanity):
    if sanity == 0:
        type_text("You spent so long in the labyrinth that you went crazy.")
        type_text("Even if you were to escape, you would never be able to reassimilate into society.")

def get_lost(num_paths):
    if num_paths == 0:
        type_text("You took so many wrong turns that you are now hopelessely lost. You will never escape.")

def lose(alive):
    if not alive:
        type_text("You weren't able to escape the labyrinth before you felt the cold hands of death\nupon you.")
        get_art(3)


#Actions
def left():
    type_text("You choose the left path.")

def right():
    type_text("You choose the right path.")

    
#Helper Functions    
def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sleep(0.03)
    print()
    
def rand_monster():
    global sanity
    global alive
    if random.randrange(0, 7) == 0:
        sanity -= 1
        type_text("After walking down the path, you hear a terrifying noise. A monster appears!")
        get_art(0)
        action = input("What will you do? (attack / run away / accept your fate) ")
        if action.lower() == "attack":
            if random.randrange(0,2) == 0:
                type_text("You vanquished the evil beast!")
            else:
                type_text("It turns out you have absolutely no idea how to fight, so now you're dead.")
                alive = False
        elif action.lower() == "run away":
            type_text("You ran as fast as your little chicken legs could carry you, but you tripped \nover a rock. You curl up into a little ball and hope the monster doesn't find \nyou.")
            type_text("Unfortunately, the monster had recently lost his glasses, so he couldn't see you\non the ground, and crushed you as he walked by.")
            alive = False
        elif action.lower() == "accept your fate":
            type_text("Wow way to stereotype. The monster was just going on a stroll and you almost \ngave him a heart attack when you screamed.")
            type_text("I hope you're proud of yourself.")
        else:
            type_text("Well the monster ran away so I guess it doesn't matter what you chose.")

def rand_win():
    global survive
    if random.randrange(0, 50) == 0:
        survive = True
        
def play():
    global alive
    global sanity
    global num_paths
    global survive
    
    type_text("You wake up with no memory of what just happened or where you are.")
    type_text("You take a look around and realize you are in the center of an elaborate\nlabyrinth, so you decide to try to find your way out.")
    
    while alive and sanity > 0 and num_paths > 0 and not survive:
        type_text("After a while, the path diverges to the left and right.")
        type_text("Will you take the left or right path? ")
        path = input()

        if "l" in path.lower():
            left()
            num_paths -= 1
        elif "r" in path.lower():
            right()
            num_paths -= 1

        if num_paths > 0:
            if num_paths % 5 == 0:
                sanity -= 1
                
        rand_win()
        rand_monster()
        go_crazy(sanity)
        get_lost(num_paths)
        lose(alive)
        win(survive)
        
start_screen()

playing = True

while playing:
    play()
    if win or not (alive and sanity > 0 and num_paths > 0):
        playing = False
