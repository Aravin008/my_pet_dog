from my_pet_dog import Dog


class Person:
    """Person class to interact with dog"""
    def __init__(self, name="John", age=12):
        self.name = name
        self.age = age
        self.dogs_affinity = {}
        self.money = 1000

    def play(self, dog):
        """person playing with dog will increase the affinity"""
        if type(dog) is Dog:
            dog.play()
            if dog not in self.dogs_affinity:
                print("Sorry, you can't play with {0}. Buy {0} to play."
                      .format(dog.name))
            else:
                self.dogs_affinity[dog][1] += 5
        else:
            print("{} can not play with it! enter valid dog object".format(self.name))

    def show_info(self):
        """display basic info about person"""
        print("{}, {} years old".format(self.name, self.age))

    def buy(self, dog):
        if type(dog) is Dog:
            if self.money >= dog.cost:
                self.dogs_affinity[dog] = [dog.name, 5]
                self.money -= dog.cost
                dog.owner = self.name
            else:
                print("you don't have enough balance.")
        else:
            print("{} can not be bought! enter valid dog object".format(self.name))

    def show_my_pets(self):
        for dog in self.dogs_affinity.keys():
            dog.get_info()
            print("has affinity {}", self.dogs_affinity[dog][1])

