import random

class Ability:  
    def __init__(self, name, attack_strength):
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
    def __init__(self, name, starting_health=100):
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

    def fight(self, opponent):
       
        # break
        
        while self.is_alive() and opponent.is_alive():
            if not self.abilities and not opponent.abilities:
                print("DRAW! ")
                return

            a1 = self.attack()
            a2 = opponent.attack()
            opponent.take_damage(a1)
            
            self.take_damage(a2)
        
            if opponent.is_alive() == False:
                print(f" {self.name} Wins! ")
                return

            elif self.is_alive() == False:
                print(f" {opponent.name} Wins!")
                return





        # function will retun the fight method between 2 instances of hero class and
         







if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.



    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 20)
    ability2 = Ability("Super Eyes", 13)
    ability3 = Ability("Wizard Wand", 8)
    ability4 = Ability("Wizard Beard", 2)
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
