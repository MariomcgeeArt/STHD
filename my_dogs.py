import dog


# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# my-dogs.py
import dog # we need to specify exactly what we want
my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)

my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()