from Carnivore import Carnivore
from Herbivore import Herbivore
from AnimalContain import AnimalContain

    # UserInterface: UserInterface
    # Animal: AnimalContain


class Controller():

    def __init__(self, UserInterface):
        self.__Animal = AnimalContain()
        self.__UserInterface = UserInterface

    def run_app(self):
        self.__UserInterface.page_info()

        menu_loop = True
        user_choice = ""
        while(menu_loop):
            self.__UserInterface.first_menu()
            print("*"*20)
            user_choice = input("Please enter a number: ")
            if user_choice == "1":
                self.add_animal()
            elif user_choice == "2":
                self.remove_animal()
            elif user_choice == "3":
                self.hunt_animal()
            elif user_choice == "4":
                self.get_info()
            elif user_choice == "5":
                self.get_all_animals()
            elif user_choice == "6":
                print("You escaped the wilderness")
                menu_loop = False
            else: 
                continue
    
    def add_animal(self):
        self.name = input("What's the name of the animal? ")
        
        try: 
            self.speed = int(input("What's the speed of the animal? "))
        
        except ValueError:
            self.__UserInterface.error
            pass

    
    def remove_animal(self):
        animals = self.__Animal.get_animals()
        print(animals)
        #choice = input("Select the name of the animal you want to remove: ")
        
    def get_all_animals(self): 
        animals = self.__Animal.get_animals()
        for animal in animals:
            print(animal)
    
    def get_info(self):
        animals = self.__Animal.get_animals()
        chosen_animal = input("Which animal do you want more information about? ")
        for animal in range(len(animals)):
            if animals[animal][0] == chosen_animal:
                print("Type of animal: {0}").format(animal[0])
                print("Speed: {0}").format(animal[1])

    def hunt_animal(self):
        pass





                



