from Animal import Animal

class Herbivore(Animal):
    #name: str
    #speed: int
    #food_source: str

    def __init__(self, food_source, *args, **kwargs):
        super().__init__(food_source, *args, **kwargs)
        self.food_source = ""

    def get_food_source(self):
        return self.food_source