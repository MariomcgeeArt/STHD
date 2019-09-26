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

    def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
            return total        


        








        
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.attack())




    # ability = Ability("Debugging Ability", 20)
    # armor = Armor("Debugging Armor", 10)
    # print(armor.name)
    # print(armor.block())
    # print(ability.name)
    # print(ability.attack())
