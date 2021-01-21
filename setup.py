import world
import os
import time
import sys
import colour

def game_setup(): #character creation
    
    os.system('cls')
    print(f"{colour.line}{colour.cyan}Mysterious Woman:{colour.end}\n")
    text = f'{colour.green}"Oh! What do we have here?!" \n"Bahahahahaaa!! Dear oh dear!" \n"Well I never!" \n"What do you call yourself?"{colour.end}'
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() 
        time.sleep(0.03) #scrolling text for when a character speaks
    world.player.name = input("\n > ") #player chooses name
    if os.path.exists(f'{world.player.name}.txt'): #if save under that name already exists
        print(f"{colour.red}A save under that name already exists!{colour.end}")
        print("Please choose a different name")
        world.player.name = input("\nName> ")#choose different name
        

    os.system('cls')
    print(f"{colour.line}{colour.cyan}Mysterious Woman:{colour.end}\n")
    text = f"{colour.green}...{colour.end}"
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush() 
        time.sleep(0.03)


    laugh = f'{colour.green}"WAHAHAHAHHAHAAAAA!  Ahhh classic..."{colour.end}'
    for char in laugh:
        sys.stdout.write(char)
        sys.stdout.flush() 
        time.sleep(0.02)

    asktrait = (f'\n {colour.green}"So tell me {colour.purple}{world.player.name}{colour.green}, would you say you are a {colour.blue}bold{colour.end} {colour.green}person or are you more {colour.blue}careful{colour.green}?"{colour.end}')
    for char in asktrait:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    world.player.trait = input("\n > ") #player chooses trait that effects available inputs and outputs
    while world.player.trait.lower() not in ['bold', 'careful']:
        print(f"Please choose '{colour.blue}bold{colour.end}' or '{colour.blue}careful{colour.end}'")
        world.player.trait = input("\n > ")
    if world.player.trait.lower() in ['bold', 'careful']:
        os.system('cls') 
        print(f"{colour.line}{colour.cyan}Mysterious Woman:{colour.end}\n")
        hmmm = f'\n{colour.green}"Interesting..."{colour.end}'
        for char in hmmm:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.04)

         

    serious = (f'{colour.green}\n"Well then {colour.purple}{world.player.name} the {world.player.trait}{colour.green} let\'s see how you fare...!"{colour.end}')
    for char in serious:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

    hehe = f'{colour.green}\n"Hehehe"{colour.end}'
    for char in hehe:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

    print("\n.")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    os.system('cls') 
    print("You awake in a small ditch with no sense of the time that has passed. You're head is pounding and there's a horrible smell...")