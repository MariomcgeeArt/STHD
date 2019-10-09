# dog.py
class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_time = sleep_time

    def sleep(self):
        print(
            "{} sleeps for {} hours {}".format(
                self.name,
                self.sleep_time))



class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")







class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")    

my_dog = Dog("Rex","SuperDog")
my_dog.bark()
# print(my_dog)
# print(my_dog.name)

my_dog = Dog("Sophie", 12)
my_dog.sleep()
my_dog.bark()
# print('hey')
newdog = Dog("rover", "pitbull")