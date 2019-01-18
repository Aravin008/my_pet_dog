""" basic_person_class to interact with dog.

    there are limited actions that can be considered for a person
    like feed, play, bath dog owned by him.
    This class also keep track of person object affinity with
    that dog object. This can be improved by playing and other actions. """
from my_pet_dog import Dog


class Person:
    """ Person class to interact with dog.

        play() : action takes one dog object as input and increase affinity
        show-info() : display user info
        buy(Dog) : to buy a dog of Dog().
        bath(Dog) : to give bath dog only if bought.
        show_my_pets() : to display all pets owned by person.
        """
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
        print("Wallet info: ${}".format(self.money))

    def buy(self, dog):
        if type(dog) is Dog:
            if self.money >= dog.cost:
                self.dogs_affinity[dog] = [dog.name, 5]
                self.money -= dog.cost
                dog.owner = self.name
                print("{} has bought {} for {} bucks"
                      .format(self.name, dog.name, dog.cost))
            else:
                print("you don't have enough balance.")
        else:
            print("{} can not be bought! enter valid dog object".format(self.name))

    def bath(self, dog):
        if type(dog) is Dog:
            self.dogs_affinity[dog][1] += 10
            dog.bath()
        else:
            print("{} can not be bought! enter valid dog object".format(self.name))

    def feed(self, dog):
        if type(dog) is Dog:
            self.dogs_affinity[dog][1] += 10
            _food_price = dog.feed()
            if _food_price:
                self.money -= _food_price
                print("{} paid {} for food".format(self.name, _food_price))
            else:
                print("{} is not hungry".format(dog.name))
        else:
            print("{} can not be bought! enter valid dog object".format(self.name))

    def show_my_pets(self):
        for dog in self.dogs_affinity.keys():
            dog.get_info()
            print("  |-has affinity {}".format(self.dogs_affinity[dog][1]))
