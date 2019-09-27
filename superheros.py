import random

class Ability:  
    def __init__(self,name,attack_strength):
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        return random.randint(0, self.max_damage)
        # may need to turn these into strings 



class Armor:
    def __init__(self, name, max_block):
        self.name = name 
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)



class Hero:
    def __init__(self,name,starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities= []
        self.armors= [] 

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

    def is_alive(self):
        alive = True
        if self.current_health > 0:
            return alive  
        elif self.current_health <= 0:
            return False    




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.

    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)


    hero = Hero("Grace Hopper", 200)
    hero.take_damage(190)
    print(hero.is_alive())
    # print(hero.current_health)
    hero.take_damage(5)
    print(hero.is_alive())

        

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
