""""my_pet_dog basic application
    Object oriented approach to create dog object
    Dog : class with relevant behaviours and state of dog
    TODO: add more behaviours/ foods/ other scenarios like ill, seasons,
        taking dog for walk outside/etc.."""
import time
import threading


class Dog:
    """ Dog : Class to create dog objects and methods perform various
        functionality

        Attributes:
        name : Name of the dog
        age: age of dog

        Methods:
        get_info() : will print name of dog and its age
        get_biggest_number() : will return the oldest dog
        is_hungry() : will check if dog is hungry
        get_food() : static function to select food for dog
        feed() : action, feeding the dog only when it is hungry
        bath() : giving bath to dog, status of dog will be updated to give bath
        mood() : method will print the happy status of dog
        play() : action, playing with the dog will make dog happy
        update_dog_status() : Method to update the dog status, over the time if
        didn't play with dog, dog will become unhappy. it will get dirty and also hungry
        TODO: add few more method to make much real. few more condition and calculation to
              update the status"""

    MAX_HUNGRY_TIME = 1000.0
    MAX_BATH_TIME = 3000.0

    def __init__(self, name="", age=0,
                 breed="Golder Ritriever", cost=200,
                 **kargs):
        self.name = name
        self.age = age
        self.breed = breed
        self.cost = cost
        # To keep track of hunger level of dog
        self.is_it_hungry = False
        self.time_of_last_food = time.time()
        # Mood of dog in percentage happy > 70 refers to being happy.
        self.happy = 50.0
        # boolean var, need to give bath if True.
        self.need_bath = False
        self.last_bath = time.time()
        # to keep track of owner
        self.owner = None
        # update_dog_status should be last so as it will be
        # called after initializing all parameters
        self.update_dog_status()

    def get_info(self):
        """"Prints Name and its age"""
        print("{} is {} years old,".format(self.name, self.age), end=' ')
        if self.owner:
            print("owned by {}".format(self.owner))
        else:
            print("owned by none.")

    def get_biggest_number(self, *args):
        """Find the oldest dog from the dog list"""
        _max_age = self.age
        for argument in args:
            if _max_age < argument.age:
                _max_age = argument.age
        print("The oldest dog is {} years old".format(_max_age))

    def is_hungry(self):
        """to check if the dog is hungry"""
        if self.is_it_hungry:
            print("\nStat : {} is hungry please feed!!".format(self.name))
        elif time.time() - self.time_of_last_food > self.MAX_HUNGRY_TIME:
            # print(time.time(), self.MAX_HUNGRY_TIME, self.time_of_last_food)
            print("\nStat : {} is hungry again!! please feed!!".format(self.name))
        else:
            print("\nStat : {} is not hungry".format(self.name))

    @staticmethod
    def get_food():
        """ This will print the menu for user to choose the food for dog
            TODO: Need to update the menu """
        print("Menu:")
        print("1. Natural Grain \t $10 \n"
              "2. Wellness Core Natural Grain Free \t $15 \n")
        _food = input("choose your food:")
        _food = ["Natural Grain", 10] if _food == '1' else ["Wellness Core Natural Grain", 15]
        return _food

    def feed(self):
        """Feeding food """
        if self.is_it_hungry:
            _food = self.get_food()
            print("\nProc: Feeding {} to {}..".format(_food[0], self.name))
            self.is_it_hungry = False
            self.time_of_last_food = time.time()
            self.happy += 10
            print("{} is full and happy".format(self.name))
            return _food[1]
        else:
            print("{} is not hungry!".format(self.name))
            return None

    def bath(self):
        """Bathing your dog"""
        if self.need_bath:
            print("\nProc : Bathing {}".format(self.name))
            self.need_bath = False
            self.last_bath = time.time()
            self.happy += 5
        else:
            print("\n {0} may not be ready to have bath or {0} is clean".format(self.name))

    def mood(self):
        """This Method will print the mood of the dog"""
        if self.happy >= 90:
            print("{} seems very happy! and Energetic!".format(self.name))
        elif self.happy >= 70:
            print("{} seems happy! and likes to play.".format(self.name))
        elif self.happy >= 50:
            print("{} is rather quite!".format(self.name))
        elif self.happy >= 25:
            print("{} is sitting in corner! consider spending time with your dog.".format(self.name))
        elif self.happy >= 5:
            print("{} is very quite seems little sad.".format(self.name))
        else:
            print("{} seems ill!")

    def play(self):
        """playing with Dog will make dog happy"""
        if self.happy < 100:
            self.happy += 3
        self.mood()

    def update_dog_status(self):
        """Method to update all the dog's status using threading concept
            this thread will be called after given interval"""
        print("Updating")
        # current time to update other status
        if self.owner:
            c_time = time.time()
            #
            if c_time - self.last_bath > self.MAX_BATH_TIME:
                self.need_bath = True
                print("{0} is dirty, {0} needs bath".format(self.name))
            if c_time - self.time_of_last_food > self.MAX_HUNGRY_TIME:
                self.is_it_hungry = True
            if self.happy >= 5:
                self.happy -= 0.25
            if self.happy in {70, 50, 25, 5}:
                self.mood()

        # to keep updating every update_rate seconds
        _timer = threading.Timer(20.0, self.update_dog_status)
        _timer.daemon = True
        _timer.start()
