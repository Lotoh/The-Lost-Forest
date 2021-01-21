import world
import sys
import setup
import os
import colour
from tkinter import *


root = Tk()
Console = Text(root)
Console.pack()

def write(*message, end = "\n", sep = " "):
    text = ""
    for item in message:
        text += "{}".format(item)
        text += sep
    text += end
    Console.insert(INSERT, text)

root.mainloop()


def main_menu_options():#menu choices
    option = input("> ")
    if option.lower() == ("new"):
        setup.game_setup() # begin new game
    elif option.lower() == ('load'):
        world.load_game() # load saved game
    elif option.lower() == ('help'):
        main_menu_help() #show help menu
    elif option.lower() == ('quit'):
        os.system('cls') # clear terminal
        sys.exit() # exit program
    while option.lower() not in ['new', 'load', 'help', 'quit']: #catch invalid input
        print(f"{colour.red}Invalid command!{colour.end}")
        option = input(f"> ")
        if option.lower() == ("new"):
            setup.game_setup() 
        elif option.lower() == ('load'):
            world.load_game() 
        elif option.lower() == ('help'):
            main_menu_help() 
        elif option.lower() == ('quit'):
            os.system('cls') 
            sys.exit()

def main_menu():#show main menu
    print("")
    print("Welcome to...")
    print("")
    print(f"{colour.purple}{colour.bold}     The Lost Forest{colour.end}")
    print("")
    print(f"   -- {colour.blue}{colour.bold}new{colour.end} --  ")
    print(f"   -- {colour.blue}{colour.bold}load{colour.end} --   ")
    print(f"   -- {colour.blue}{colour.bold}help{colour.end} --   ")
    print(f"   -- {colour.blue}{colour.bold}quit{colour.end} --   ")
    print("")
    print("#   Type your command and press Enter!  #")
    main_menu_options()

def main_menu_help():# help menu
    os.system('cls')
    print("")
    print(f" --- {colour.purple}{colour.bold}Help{colour.end} --- ")
    print("")
    print("Follow the instructions on screen!")
    print("")
    print(f"Pick from the list of given {colour.blue}commands{colour.end}. Type the {colour.blue}command{colour.end} and then press enter to execute!")
    print("")
    print(f"E.g. To navigate the world, type {colour.blue}move{colour.end} and press enter. Then type '{colour.blue}north{colour.end}', '{colour.blue}south{colour.end}', '{colour.blue}west{colour.end}' or '{colour.blue}east{colour.end}' as prompted and press enter. You will then move in that direction to a new location. You can only move when the option is given")
    print("")
    print("A grid map will show your current position. You are the 'x'")
    print("")
    print(f"Use the '{colour.blue}search{colour.end}' command to find items and add them to you inventory!")
    print("")
    print(f"Choose the '{colour.blue}use{colour.end}' command to use an item that is in your inventory. Some items do different things depending on your situation...")
    print("")
    print(f"Use '{colour.blue}save{colour.end}' to store your character and game state.")
    print("")
    print(f"Your save games can be loaded from the main menu by selecting '{colour.blue}load{colour.end}' and typing the name of the character whose game you want to load")
    print("")
    print("Good luck!")
    print("")
    print("#   Type your command and press Enter!  #")
    print("")
    option = input(f"  -- Please type '{colour.blue}new{colour.end}' to start a new game, '{colour.blue}load{colour.end}' to load an existing game, or '{colour.blue}back{colour.end}' to return to the main menu --\n  \n> ")
    print("")
    if option.lower() == ("new"):
        setup.game_setup() # begin new game
    elif option.lower() == ('load'):
        world.load_game() # load saved game
    elif option.lower() == ('back'):
        os.system('cls') # clear terminal
        main_menu() # back to main menu
    while option.lower() not in ['new', 'load', 'back']: #catch invalid input
        print(f"{colour.red}Invalid command!{colour.end}")
        option = input(f"> ")
        if option.lower() == ("new"):
            setup.game_setup() 
        elif option.lower() == ('load'):
            world.load_game() 
        elif option.lower() == ('back'):
            os.system('cls') 
            main_menu()
