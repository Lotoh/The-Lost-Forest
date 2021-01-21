import os
import colour
import world

class completion:#task completion 
    def __init__(self, done, description):
        self.done = done
        self.description = description
    
    def mark_done(self):
        self.done = True




class character: #general character class (used as is for boss)
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, enemy): #attack function
        damage = (self.power)
        enemy.damage(self, damage)
        print(f"{colour.red}{self.name} attacks {enemy.name} dealing {damage} damage!{colour.end}")


    def damage(self, enemy, damage): #damage function
        self.hp -= damage

        if self.hp <= 0: #if health falls to zero it's game over
            os.system('cls')
            print(f"{colour.red}** {self.name} has died! **{colour.end}")#if player kills boss
            print(f"{colour.purple}** You pass out **{colour.end}")#purple colour for boss death
            print("")
            world.game_end()#call game ending function


            
    def hp_increase(self): #add 2 health (when player uses raisins)
        self.hp += 2

    def power_increase(self): #add 1 power (when player uses the fetching hat)
        self.power += 1

    def enrage(self): #boss now has +5 power 
        self.power += 5

    def frogged(self):#minus 1 health (after being robbed by Cecil the frog)
        self.hp -= 1 



class player_character (character): #player specific 'character' class with inheritance from 'character' class
    def __init__(self, name, hp, power, trait, inventory, location):
        super().__init__(name, hp, power)
        self.trait = trait
        self.inventory = inventory
        self.location = location

    def damage(self, enemy, damage): #damage function specific to player
        self.hp -= damage

        if self.hp <= 0: #if health falls to zero it's game over
            os.system('cls')
            print(f"{colour.red}** {self.name} has died! **{colour.end}")#if player dies
            print(f"{colour.red}** GAME OVER **{colour.end}")#red colour for player death
            print("")
            world.game_end()#call game ending function

    























