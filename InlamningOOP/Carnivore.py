from Animal import Animal
from Herbivore import Herbivore

class Carnivore(Animal):

    def __init__(self, prey_list, *args, **kwargs):
        super().__init__(prey_list, *args, **kwargs)
        self.prey_list = []

    def get_prey_list(self):
        return self.prey_list

    def hunt_animal(self, Herbivore ):
        #for animal in self.prey_list:
        pass
        ''' if input == in [Carnivore, Herbivore] return animal '''