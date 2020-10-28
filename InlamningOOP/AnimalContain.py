from Animal import Animal

class AnimalContain(Animal):

    def __init__(self):
        self.animals = []

    def get_animals(self):
        return self.animals

    def get_name(self, animal):
        return animal.get_name()

    def get_food_source(self, animal):
        return animal.get_food_source()
    
    def get_prey_list(self, animal):
        return animal.get_prey_list()
    
    def get_speed(self, animal):
        return animal.get_speed()
    
    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def hunt_animal(self, animal):
        pass
        ''' Hunt animal '''