from abc import abstractmethod, ABC

class Animal(ABC):

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed

    def get_name(self):
        return self.name
    
    def get_speed(self):
        return self.speed

    @abstractmethod
    def get_food_source(self):
        pass

    @abstractmethod
    def get_prey_list(self):
        pass


    def __str__(self):
        return ('Animal name: {0}, Speed: {1}').format(self.name, self.speed)
