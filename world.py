import classes
import textwrap
import shutil
columns, rows = shutil.get_terminal_size()
import sys
import time
import os
import random
import pickle
import menu
import colour




def save_game():#save function
        saveGame = open(f'{player.name}.txt', 'wb') #write new save file. text file named by the player
        saveValues = (player.name, player.hp, player.power, player.trait, player.inventory, player.location, task1.done, task2.done, task3.done, task4.done, task5.done, game_map['ditch'], game_map['thicket'], game_map['big tree'], game_map['clearing'], game_map['hut'], game_map['pond'])#values to save
        pickle.dump(saveValues, saveGame) #serialize
        saveGame.close()#close file
        os.system('cls') 
        print(f"Game saved as: {colour.purple}{player.name}{colour.end}")
        player_action


def load_game():#load function
    os.system('cls')
    load = input ("Load whose game?\n > ") #asks player for the name of the save file (players chosen name)
    if os.path.exists(f"{load}.txt"): #if a file of that name exists..
        loadGame = open(f'{load}.txt', 'rb') #...open it
        loadValues = pickle.load(loadGame) #deserialize
        player.name = loadValues[0] #set player.name to index 0 of saveValues(from save function)
        player.hp = loadValues[1] #set player.hp to index 1 of saveValues(from save function)
        player.power = loadValues[2]
        player.trait = loadValues[3]
        player.inventory = loadValues[4]
        player.location = loadValues[5]
        task1.done = loadValues[6]
        task2.done = loadValues[7]
        task3.done = loadValues[8]
        task4.done = loadValues[9]
        task5.done = loadValues[10]
        game_map['ditch'] = loadValues[11]
        game_map['thicket'] = loadValues[12]
        game_map['big tree'] = loadValues[13]
        game_map['clearing'] = loadValues[14]
        game_map['hut'] = loadValues[15]
        game_map['pond'] = loadValues[16]
        loadGame.close()
        os.system('cls') 
        print(f"Loaded {colour.purple}{load}'s{colour.end} saved game") #print what file has been loaded
        player_action #player action choices
    else:
        print("No save with that name exists!")
        menu.main_menu() #if no save under that name exists, go back to main menu
        

player = classes.player_character("", 10, 2, "", [], "ditch")#player character
boss = classes.character("Mysterious Woman", 6, 4) #Mysterious woman / Boss


#possible tasks to complete
task1 = classes.completion(False, 'Found and ate the raisins') #raises player hp
task2 = classes.completion(False, 'Wore the fetching hat') #raises player power and needed to reason with the boss
task3 = classes.completion(False, 'Revealed the key') #required for progression
task4 = classes.completion(False, 'Entered the hut') #required for progression
task5 = classes.completion(False, 'Robbed by Cecil') #throw two rocks into the pond to suffer the wrath of Cecil
task6 = classes.completion(False, 'Enraged the Mysterious Woman') #Lie to the mysterious woman about disturbing Cecil
task7 = classes.completion(False, 'Succesfully reasoned with the Mysterious Woman') #Choose the 'reason' option in the final battle whiel wearing the hat and having the raisins (good ending)





description = 'description'
item = 'item'
north = 'north'
south = 'south'
west = 'west'
east = 'east'
grid = 'grid'
grid2 = 'grid2'
grid3 = 'grid3'
additem = 'additem'


game_map = {
    'ditch': {
        description : '-- A conveniently soft and hidden ditch. Feels safe.\n \nTo your north there is an area of thick bush.\nTo your east is a small pond',
        item : 'raisins',#item in this location
        north : 'thicket',#if player moves north from the ditch they go to the thicket
        east : 'pond',#if player moves east from the ditch they go to the thicket
        grid : '- -',#shows the map as a grid
        grid2 : '- -',#shows the map as a grid
        grid3 : 'x -',# x shows the player location
    },
    
    'thicket': {

        description : '-- Trees all around you block the light. An eerie wind sends a chill down your spine...\n \nTo the north there is a huge tree.\nTo your south is the ditch you started in.\nTo the east is a small hut.',
        item : 'fetching hat',
        north : 'big tree',
        south : 'ditch',
        east : 'hut',
        grid : '- -',
        grid2 : 'x -',
        grid3 : '- -',
    },

    'big tree': {
        description : '-- It\'s like a tree, but bigger. The gigantic being towers above the forest. The tree is dry and it\'s bark is temptingly loose...\n \nTo the south is an area of thick bush.\nTo the east is a clearing in the forest.',
        item : 'key',
        south : 'thicket',
        east : 'clearing',
        grid : 'x -',
        grid2 : '- -',
        grid3 : '- -',
    },


    'clearing': {
        description : '-- A break in the trees. A large area carpeted by green grass and wild flowers. There are small rocks everywhere...\n \nTo the south is a small hut.\nTo the west is a huge tree.',
        item : 'rock',
        south : 'hut',
        west : 'big tree',
        grid : '- x',
        grid2 : '- -',
        grid3 : '- -',
    },

    'hut': {
        description : '-- A small hut in the middle of the forest. It seems somewhat out of place. The sturdy door is locked...\n \nTo the north is a clearing in the forest.\nTo the south is a small pond.\nTo the west is an area of thick bush.',
        item : [],
        north : 'clearing',
        south : 'pond',
        west : 'thicket',
        grid : '- -',
        grid2 : '- x',
        grid3 : '- -',
    },

    'pond': {
        description : '-- An uninviting pond covered in green scum. Bubbles periodically appear on the surface. You wonder what\'s beneath...\n \nTo the north is a small hut.\nTo the west is the ditch you started in.',
        north : 'hut',
        west : 'ditch',
        grid : '- -',
        grid2 : '- -',
        grid3 : '- x',
        additem : [],
    },

    '???': {#final area
        description : 'You can\'t see anything',
        north : '???',#moving from the area is impossible
        west : '???',
        south : '???',
        east : '???',
        grid : '? ?',# no player location shown
        grid2 : '? ?',
        grid3 : '? ?', 
    }

}                

def describe_area(): #print the value from the key 'description' in game_map[player.location] dictionary
    print(f"{game_map[player.location][description]}")

    
def player_action():# Presents information and player action options
    print(f"\n-- You are at the {colour.purple}{player.location}{colour.end} --")#shows the player's current location
    describe_area()# prints the description from game_map corresponding to the current player location
    print("")
    print(f"   // {game_map[player.location][grid]} //")# prints grid map
    print(f"   // {game_map[player.location][grid2]} //")# prints grid map
    print(f"   // {game_map[player.location][grid3]} //")# prints grid map
    print("")
    print(f"-- Player: {colour.purple}{player.name}{colour.end}")#print current player name
    print(f"-- Stats: {colour.red}Health{colour.end}: {player.hp} {colour.red}Power{colour.end}: {player.power}")#print current player health and power
    print(f"-- Inventory:{colour.yellow}{player.inventory}{colour.end}")#print current player inventory
    
    print("")
    print("\nWhat do you want to do?")#shows player choices
    print("")
    print(f"   -- {colour.blue}move{colour.end} --  ")
    print(f"   -- {colour.blue}search{colour.end} --   ")
    print(f"   -- {colour.blue}use{colour.end} --   ")
    print(f"   -- {colour.blue}quit{colour.end} --   ")
    print(f"   -- {colour.blue}save{colour.end} --  ")
    print("")
    action = input ("> ")   
    allowed = ['move', 'quit', 'search', 'use', 'save'] #valid inputs
    while action.lower() not in allowed: #if input is not in valid inputs
        print(f"{colour.red}Invalid commmand.{colour.end} Enter '{colour.blue}move{colour.end}', '{colour.blue}search{colour.end}', '{colour.blue}use{colour.end}', '{colour.blue}save{colour.end}', '{colour.blue}quit{colour.end}' \n")
        action = input ("> ")  #ask for input again
    if action.lower() == 'quit':
        os.system('cls') 
        sure_quit = input(f"Enter '{colour.blue}quit{colour.end}' again to go to the {colour.purple}main menu{colour.end} or any key to cancel\n> ")#quit check
        if sure_quit.lower() == 'quit':#quit to main menu
            os.system('cls')
            menu.main_menu()#back to main menu
        else:
            os.system('cls') #anything other than quit takes you back
            player_action()

    elif action.lower() == 'move':
        player_move(action.lower())#calls move function
    elif action.lower() == 'search':
        player_search()#calls search function
    elif action.lower() == 'use':
        player_use()#calls use functioon
    elif action.lower() == 'save':
        save_game() # calls save function


def player_search():#search option from player_action. Determines what the 'search; function does in certain situations
    os.system('cls') 
    if item in game_map[player.location] and player.location == 'ditch': #if 'item' key has a value in 'ditch' dictionary
        player.inventory.append(game_map[player.location][item])#add the 'item' value from the 'ditch' dictionary in world.game_map (raisins) to player inventory
        del game_map[player.location][item] #remove the 'raisins' from the 'ditch'
        print(f"You shuffle around in the ditch and find your box of {colour.yellow}raisins{colour.end}! Must've fallen out...")
        print("")
        print(f"{colour.red}** Raisins added to your inventory **{colour.end}")
    
    elif item in game_map[player.location] and player.location == 'big tree' and task3.done == False: #if player tries to search at 'big tree' before succesfully 'using' 'rock' here. Gives a hint.
        print("The bark looks brittle but you can't get it off with just your hands...")

    elif item in game_map[player.location] and player.location == 'big tree' and task3.done == True: #if player has 'used' rock successfully at 'big tree' and key is revealed
        player.inventory.append(game_map[player.location][item]) #add key to player inventory
        del game_map[player.location][item] #remove key from location
        print(f"You brush away the broken bark and reach inside...you found a {colour.yellow}key{colour.end}!")
        print("")
        print(f"{colour.red}** Key added to you inventory! **{colour.end}")

    elif item in game_map[player.location] and player.location == 'clearing':
        player.inventory.append(game_map[player.location][item])#rock added to player inventory. item not removed from location and can be repeated.
        print(f"You picked up a {colour.yellow}rock{colour.end}")
        print("")
        print(f"{colour.end}** Rock added to inventory! **{colour.end}")
           

    elif item in game_map[player.location] and player.location == 'thicket':
        player.inventory.append(game_map[player.location][item])
        del game_map[player.location][item]
        print(f"In a particularly dense bush you spot a {colour.yellow}fetching hat{colour.end}. It looks brand new!")
        print("")
        print(f"{colour.red}** Fetching Hat added to you inventory! **{colour.end}")

    elif player.location == '???': #needed to progress
        print("You reach out into the darkness with your hand...")
        time.sleep(3)
        finale()# go to ending section

    else:
        print("Nothing...")#no item available upon 'search'
        text = "\n Unless..."
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.2)
        print("Nope, nothing.")


def player_use(): #use option from player_action. Determines what the 'use' option does in certain situations
    os.system('cls')
    use = input(f"What do you want to use?\n \n{colour.yellow}Inventory: {player.inventory}{colour.end}\n \n(or any input to go back)\n \n> ")
    if use.lower() not in player.inventory: #if none in inventory go back
        os.system('cls') 
        print(f"You don't have a {colour.red}{use}{colour.end}...")
        player_action()
    elif use.lower() == 'raisins' and task1.done == False: #if player hasn't 'used' the raisins yet. Doesn't remove 'raisins' from inventory 
        os.system('cls') 
        print(f"You eat a few {colour.yellow}raisins{colour.end}")
        task1.done = True #player has now 'used' the raisins and task1 is completed
        text = "Mmmmm...juicy..." 
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print(f"\nThe {colour.yellow}raisins{colour.end} have increased your hp!")
        player.hp_increase() #function from classes.character called to raise player.hp by 2. Cannot be repeated
    elif use.lower() == 'raisins' and task1.done == True: #if player has alraedy 'used' raisins. To avoid repeated health additions
        os.system('cls')
        print(f"That's enough {colour.yellow}raisins{colour.end} for now...")
    elif use.lower() == 'fetching hat' and task2.done == False: #if player has yet to 'use' the 'fetching hat'
        os.system('cls')
        print(f"You place the {colour.yellow}fetching hat{colour.end} on your head.")
        print("You look great")
        time.sleep(2)
        print("Not silly at all.")
        time.sleep(3)
        print(f"{colour.red}**You are now wearing the {colour.yellow}fetching hat{colour.red}**{colour.end}")
        print(f"The {colour.yellow}fetching hat{colour.end} has increased your power by 1!")
        player.inventory.remove('fetching hat') #removed from inventory to avoid repeated power increases and theft from Cecil at the 'pond'
        player.power_increase() #function to increase player power by 1 called (from classes.character)
        task2.done = True #player is now wearing the 'fecthing hat' and task 2 is complete

    
    elif use.lower() == 'rock' and player.location == 'pond' and 'rock' in game_map[player.location][additem]:#if player has previously thrown a rock into the pond
        os.system('cls') 
        print(f"You throw another {colour.yellow}rock{colour.end} into the pond. The smelly, slimey frog-man leaps out again and stares at you menacingly")
        player.inventory.remove('rock') #player has 'used' the item, remove it from player inventory
        if player.trait.lower() == 'careful': #branch for if 'careful' trait was chossen during setup.game_setup
            valid = ['sorry', 'run']
            response = input(f"What will you do?\nSay {colour.blue}sorry{colour.end} or {colour.blue}run{colour.end} away?\n>")
            while response.lower() not in valid:
                response = input(f"Use '{colour.blue}sorry{colour.end}' to apologise to the frog-man or '{colour.blue}run{colour.end}' to run away\n>")
            if response.lower() == 'run': #unique option for 'careful' trait holder
                os.system('cls')
                print(f"{colour.red}**  You turn tail and run back to the ditch!  **{colour.end}")
                player.location = game_map[player.location][west] #player location changed to 'ditch'
            elif response.lower() == 'sorry':
                os.system('cls')
                print("The frog-man softens his stare for a moment before letting out a mighty croak and rushing towards you. Quick as a flash he rushes up to you and then dives back into the pond.")
                print(f"{colour.red}** You lost 1 health! **{colour.end}")
                player.frogged()#function from classes.chracter called to remove 1 health from player. Can be repeated
                if 'key' in player.inventory:#player needs to keep key to progress
                    player.inventory = ['key'] #if player had the key, it is not lost.
                    print(f"{colour.red}He stole everything...except for the {colour.yellow}key{colour.end}...")
                    task5.done = True #Robbed by Cecil the frog-man and task5 in complete.
                else:
                    player.inventory = [] #inventory emptied
                    print(f"{colour.red}** Everything in your inventory is gone! **{colour.end}")
                    task5.done = True #Robbed by Cecil the frog-man and task5 in complete.

        elif player.trait.lower() == 'bold': #branch for if player chose 'bold' trait at character creation
            valid = ['sorry', 'stare']
            response = input(f"What will you do?\nSay {colour.blue}sorry{colour.end} or {colour.blue}stare{colour.end} back?\n>")
            while response.lower() not in valid:
                response = input(f"Use '{colour.blue}sorry{colour.end}' to apologise to the frog-man or '{colour.blue}stare{colour.end}' to antagonize?\n>")
            if response.lower() == 'sorry':
                os.system('cls')
                print("The frog-man softens his stare for a moment before letting out a mighty croak and rushing towards you. Quick as a flash he rushes up to you and then dives back into the pond.")
                print(f"{colour.red}** You lost 1 health! **{colour.end}")
                player.frogged() #function from classes.chacracter called to reduce player health by 1. Can be repeated
                if 'key' in player.inventory:#player needs to keep key to progress
                    player.inventory = ['key']#if player had the key, it is not lost.
                    print(f"{colour.red}He stole everything...except for the {colour.yellow}key{colour.end}...")
                    task5.done = True #Robbed by Cecil the frog-man and task5 in complete.
                else:
                    player.inventory = []
                    print(f"{colour.red}** Everything in your inventory is gone! **{colour.end}")
                    task5.done = True #Robbed by Cecil the frog-man and task5 in complete.
            elif response.lower() == 'stare': #unique option for 'bold' trait holder
                os.system('cls')
                print("You stare right back. The frog-man is enraged and rushes towards you. Before you can even react he's on you and is back in the pond")
                print(f"{colour.red}** You lost 1 health! **{colour.end}")
                player.frogged()
                if 'key' in player.inventory:
                    print(f"{colour.red}He stole everything...except for the {colour.yellow}key{colour.yellow}...")
                    player.inventory = ['key']
                    task5.done = True
                else:
                    print(f"{colour.red}** Everything in your inventory is gone! **{colour.end}")
                    player.inventory = []
                    task5.done = True


    elif use.lower() == 'rock' and player.location == 'pond': #'use' a rock at the pond for the first time
        os.system('cls') 
        print(f"You throw a {colour.yellow}rock{colour.end} into the pond. The bubbles intensify and and a smelly, slimey frog-man leaps out! He sees you and shouts angrily before slipping back under the water.\n{colour.bold}Better not do that again!{colour.end}")
        player.inventory.remove('rock') #'rock' is 'used' and removed from player.inventory
        game_map[player.location][additem].append('rock')#add rock to pond dictionary to track if rock has been thrown into pond

    elif use.lower() == 'rock' and player.location == 'big tree' and task3.done == False: #if player hasn't revealed the key yet. Must complete to progress
        os.system('cls')
        print(f"You throw a {colour.yellow}rock{colour.end} at the tree, aiming for a particular knot")
        chance = random.randint(0, 10)#random number to determine hit or miss
        throw = ". . ."
        for char in throw:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.3)
        player.inventory.remove('rock')
        if (chance <= 4):#chance to hit
            os.system('cls')
            print("You hit the mark and take a chunk out of the bark") #successful throw 
            print(f"You can see {colour.yellow}something{colour.end} shining in the hole you made...")
            task3.done = True #revealed the key and task3 is complete
        elif (chance >= 6):#chance to miss
            os.system('cls')
            print(f"You miss the shot, but {colour.yellow}something{colour.end} compels you to keep trying...") #unsucessful
              
    elif use.lower() == 'rock' and player.location == 'big tree' and task3.done == True: #if player has already revealed the 'key'
        os.system('cls')
        print(f"You have already smashed the poor tree, maybe you should {colour.blue}search{colour.end} the hole you made?")
    
    elif use.lower() == 'rock' and player.location == 'hut':#cannot smash 'hut' door with 'rock'
        os.system('cls')
        print(f"Your puny {colour.yellow}rock{colour.end} is no match for the sturdy door...")

    elif use.lower() == 'rock' and player.location == '???':
        os.system('cls')
        print(f"You throw a {colour.yellow}rock{colour.end} into the darkness.")
        player.inventory.remove('rock')
        throw = ". . .\n"
        for char in throw:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.5)
        print("There is no sound. Did the rock meet the floor? Is there a floor? Did you even throw the rock!?")


    elif use.lower() == 'key' and player.location == 'hut':#use 'key' at the 'hut'
        os.system('cls') 
        print(f"You approach the hut and pull out the {colour.yellow}key{colour.end}. As you go to unlock the door a sense of dread washes over you...")
        print("")
        go_stay = ['go', 'stay']
        decision = input(f"What will you do? {colour.blue}go{colour.end} or {colour.blue}stay{colour.end}?\n>")
        while decision.lower() not in go_stay:
            decision = input(f"What will you do? '{colour.blue}go{colour.end}' or '{colour.blue}stay{colour.end}'?\n>")
        if decision.lower() == 'go': #proceed (player cannot return)
            task4.done = True #key used to enter the 'hut'. task4 complete.
            os.system('cls')
            print("You unlock the door and enter. To your surprise you\'re greeted with a grand hallway. It's huge!")
            time.sleep(1)
            if player.trait.lower() == 'bold': #branch for 'bold' trait holder
                time.sleep(5)
                print(f"The oddness of the situation is not lost on you but your {colour.purple}boldness{colour.end} overrides any doubt you might have.")
                time.sleep(3)
                print("You start making your way down the hall.")
                time.sleep(2)
                run = ". . . . .\n"
                for char in run:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.3) #normal walking for 'bold' individual
            elif player.trait.lower() == 'careful': #branch for 'careful' trait holder
                print(f"You pause for a moment and {colour.purple}carefully{colour.end} consider your situation. This place couldn't be more strange...something doesn't feel right...")
                time.sleep(4)
                print("You turn around to exit but the door is gone!")
                time.sleep(4)
                print("You have no choice but to walk down the seemingly endless hall...")
                time.sleep(2)
                walk = ". . . . .\n" 
                for char in walk:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(1) #slower walking for 'careful' individual                


            print("The shadows from the wall-mounted candles flutter all around and your footsteps echo loudly as you walk")
            time.sleep(4)
            print("Suddenly, you are plunged into darkness. You can't see an inch in front of you")
            player.location = '???' #player location changed
            player_action() #information and options presented
        elif decision.lower() == 'stay':
            os.system('cls')
            player_action() #location remains 'hut'. Information and options presented
    else:
        os.system('cls') 
        print(f"{colour.red}No use for that here{colour.end}") #item is in inventory but has no use in current situation

        
def player_move(action): #'move' option from player_action

    direction = input(f"What direction do you want to go? Choose {colour.blue}north{colour.end}, {colour.blue}south{colour.end}, {colour.blue}east{colour.end} or {colour.blue}west{colour.end} (check map for suitable directions) \n> ")
    os.system('cls')
    if direction.lower() not in game_map[player.location]:
        os.system('cls')
        print(f"You cannot go {colour.red}'{direction}'{colour.end}...") 
        time.sleep(3)
        os.system('cls')
        player_action()
    elif direction.lower() == 'north':
        os.system('cls') 
        destination = game_map[player.location][north] #destination(used in following move_func) is set by the value for the 'north' key in the game_map[player.location] disctionary
        move_func(destination) #player moves to destination
    elif direction.lower() == 'south':
        os.system('cls') 
        destination = game_map[player.location][south]
        move_func(destination)
    elif direction.lower() == 'west':
        os.system('cls') 
        destination = game_map[player.location][west]
        move_func(destination)
    elif direction.lower() == 'east':
        os.system('cls') 
        destination = game_map[player.location][east]
        move_func(destination)
    elif direction.lower() == 'back':
        os.system('cls') 
        player_action()

def move_func(destination): #function for changing player location as chosen in player_move function
    player.location = destination





def finale():#final section
    print("")
    text = f'{colour.green}"Well, well, well. You took your time."{colour.end}'
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")
    print("\nIt's the woman from earlier! She\'s right in front of you! You're sure she wasn't there a moment ago...")
    time.sleep(2)
    print("")
    if task5.done == True: #if player was robbed by Cecil the frog-man at the 'pond'
        print(f"{colour.cyan}{colour.line}Mysterious Woman:{colour.end}")
        ask = (f'{colour.green}\n"You look a little beaten up"\n..."You didn\'t disturb Cecil at the pond did you!?"{colour.end}')
        for char in ask:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)
        print("")
        print("Cecil!? Does she mean the frog-man? She sounds angry...")
        print("")
        yes_no = ['yes', 'no']
        no_lie = input(f"Say {colour.blue}yes{colour.end} or {colour.blue}no{colour.end}\n> ")
        while no_lie.lower() not in yes_no:
            no_lie = input(f"Say {colour.blue}yes{colour.end} or {colour.blue}no{colour.end}\n> ")
        if no_lie.lower() == 'yes':#player doesn't lie, no change, go to battle
            os.system('cls')
            print(f"{colour.cyan}{colour.line}Mysterious Woman:{colour.end}")
            hoho = f'{colour.green}"Hohoha, he is a grumpy one!"{colour.end}'
            for char in hoho:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.05)
            text = f'{colour.green}"\nWell...\nYou\'ve done so well to make it this far...\n...but your time here is now over!"{colour.end}'
            time.sleep(2)
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.08)
            battle()#battle starts
        elif no_lie.lower() == 'no': #player lies
            os.system('cls')
            task6.mark_done() #player lied to Mysterious Woman and enrages her. task6 completed
            boss.enrage() #function to increase boss.power by 5 called due to player lie
            print(f"{colour.cyan}{colour.line}Mysterious Woman:{colour.end}")
            text = (f'{colour.green}"...I see"{colour.end}')
            for char in text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.04)
            time.sleep(1)
            scream = f'{colour.green}\n"RAARHGAHGHRGHAGRARGHAGRA!"{colour.end}'
            for char in scream:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.02)
            battle() #start battle
    else:
        print(f"{colour.cyan}{colour.line}Mysterious Woman:{colour.end}")
        text = f'{colour.green}"I suppose you\'ve done well to make it this far...\n...but your time is now up!"{colour.end}'
        time.sleep(2)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.08)
        battle()


def battle():#final battle
    os.system('cls')
    print("She lunges towards you and swipes at your head")
    boss.attack(player) #unavoidable attack from boss
    print("")
    print(f"{colour.purple}{player.name} the {player.trait}{colour.end} VS {colour.cyan}The Mysterious Woman!{colour.end}")
    print("")
    while True:
        battle_action() #call battle_action function to begin final battle


def battle_action():#final battle action
    print(f"You have {colour.red}{player.hp} health{colour.end} left") #shows player health after each attack
    b_action = input(f"What will you do? {colour.blue}attack{colour.end} or try to {colour.blue}reason{colour.end} with her?\n> ")
    while b_action.lower() not in ["attack", "reason"]:
        b_action = input(f"What will you do? {colour.blue}attack{colour.end} or {colour.blue}reason{colour.end}?\n> ")
    if b_action.lower() == "attack":
        print("")
        player.attack(boss) #you attack the boss
        boss.attack(player) #the boss attacks back each time player chooses to 'attack'
    elif b_action.lower() == "reason": #reasoning with the boss is only successful if player is wearing the 'fetching hat'(task2) and has 'raisins' in inventory
        if task2.done == True:
            print(f"The {colour.yellow}fetching hat{colour.end} you are wearing seems to mesmerise the woman. Words seem to flow directly from it and out of your mouth.")
            time.sleep(3)
            print("\n")
            print(f"The {colour.cyan}The Mysterious Woman{colour.end} seems to calm slightly. She seems conflicted and rage starts to build once again")
            time.sleep(4)
            if 'raisins' in player.inventory:
                print("")
                print(f"You pull out your {colour.yellow}raisins{colour.end} as a desperate peace offering")
                time.sleep(3)
                print("")
                print("She looks at your offering for a few seconds before excitedly snatching them from you")
                time.sleep(3)
                os.system('cls')
                print(f"{colour.cyan}{colour.line}Mysterious Woman:{colour.end}")
                hehe = f'{colour.green}"hehehe"'
                for char in hehe:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.5)

                haha = '\n"Ha Haha Haha"'
                for char in haha:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.3)

                goodbye = f'"\nMWUAHAHAHAHAHAHAHAHAHAHAHAHAHA!"{colour.end}'
                for char in goodbye:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

                print("\nThe woman disappears into the darkness with your raisins!") 
                print("")
                time.sleep(3)
                print("You feel your consciousness slipping...")
                print("")
                time.sleep(3)
                task7.mark_done() # sucessfully reasoned with the mysterious woman(boss) task7.done == True
                print(f"{colour.green}Congratulations!{colour.end}") #good ending
                game_end()

            else:
                print(f"{colour.cyan}{colour.line}Mysterious Woman:{colour.end}")
                print("Rararhgarhagrhgh!") #back to battle_action()
                boss.attack(player)
        else:
                print(f"{colour.cyan}{colour.line}Mysterious Woman:{colour.end}")
                print("Rararhgarhagrhgh!") #back to battle_action()
                boss.attack(player)


def game_end(): #called to end the game if player dies, boss dies or boss is reasoned with.
    print(f"{colour.purple}Thank you for playing!{colour.end}")
    print("")
    print("\n**Tasks completed**")#shows which tasks were completed during the playthrough 
    print("")
    print(f"{task1.description} = {task1.done}")
    print(f"{task2.description} = {task2.done}")
    print(f"{task3.description} = {task3.done}")
    print(f"{task4.description} = {task4.done}")
    print(f"{task5.description} = {task5.done}")
    print(f"{task6.description} = {task6.done}")
    print(f"{task7.description} = {task7.done}")

    

    print("")
    end = input(f"Enter {colour.blue}quit{colour.end} to exit\n> ")
    if end.lower() == 'quit':
        os.system('cls')
        menu.main_menu()
    else:
        end = input(f"Enter {colour.blue}quit{colour.end} to exit\n> ")

    

                
        

            



