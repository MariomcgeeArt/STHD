import random

class Ability:  
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        return random.randint(0, self.max_damage)
        # may need to turn these into strings 

class Weapon (Ability):
    def attack(self):
        return random.randint(self.max_damage // 2, self.max_damage)


class Armor:
    def __init__(self, name, max_block):
        self.name = name 
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)



class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.kills = 0
        self.deaths = 0
        self.abilities= []
        self.armors= []

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)     

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total
            
    def defend(self, damage_amt=0):
        blocked = 0
        for armor in self.armors:
            blocked += armor.block()
        return abs(blocked - damage_amt)

    def take_damage(self, damage=0):
        hit = self.defend(damage)
        self.current_health = self.current_health - hit

    def add_kill(self,num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

    def is_alive(self):
        alive = True
        if self.current_health > 0:
            return alive  
        elif self.current_health <= 0:
            return False

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            if not self.abilities and not opponent.abilities:
                print("DRAW! ")
                return

            # v1 = self.attack()
            # v2 = opponent.attack()
            opponent.take_damage(self.attack())
            
            self.take_damage(opponent.attack())
            
            if opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_deaths(1)
                print(f" {self.name} Wins! ")
                print(f"{opponent.name} is DEAD! ")
                return

            elif self.is_alive() == False:
                opponent.add_kill(1)
                self.add_deaths(1)
                print(f" {opponent.name} Wins! ")
                print(f"{self.name} is DEAD! ")
                return

class Team:
    def __init__(self,name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for name in self.heroes:
            self.heroes.remove(name)
        else:
            return 0

    def view_all_heroes(self):
        for index, list_item in enumerate(self.heroes):
            print("{} {}".format(index, list_item.name))

    def add_hero(self, hero):
        self.heroes.append(hero)

    def get_alive(self):
        alive = []
        for heroes in self.heroes:
            if heroes.is_alive():
                alive.append(heroes)
        return alive

    def attack(self, other_team):

        while len(self.get_alive()) > 0 and len(other_team.get_alive()) > 0:
            H1 = random.choice(self.get_alive())
            H2 = random.choice(other_team.get_alive())
            H1.fight(H2)
                   
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        for hero in self.heroes:
            print(f"{hero.name} has K/D of {hero.add_kills()} {hero.add_deaths()} ! ")
            


class Arena:
    def __init__(self):
        self.team_one = none
        self.team_two = none

    def create_ability(self):
        name = input("Give your Hero an Ability!: ")
        power = int(input('Give the Ability a power level: '))
        ability = Ability(name,power)
        return ability

    def create_weapon(self):
        name = input("Give your Hero a Weapon!: ")
        power = int(input('Give the Weapon a power level: '))
        weapon = Weapon(name,power)
        return weapon


        



























if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.



    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)









    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)


    # hero = Hero("Grace Hopper", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # # print(hero.current_health)
    # hero.take_damage(1500)
    # print(hero.is_alive())

        

    # fire = Ability("Fire",20)
    # hero1 = Hero('Hero1',200)
    # hero1.add_ability(fire)
    # # OOP example printing out objects attribute 
    # print(hero1.abilities[0].name)










    # ability = Ability("Debugging Ability", 20)
    # armor = Armor("Debugging Armor", 10)
    # print(armor.name)
    # print(armor.block())
    # print(ability.name)
    # print(ability.attack())
