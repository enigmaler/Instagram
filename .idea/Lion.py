from Animal import Animal
from AbsOfAnimal import Abs_Animal

emilbek = "Eimlbek"

class Lion(Animal, Abs_Animal):

    emilbek = ("emilbek")
    def __init__(self, age, skin_color, isMale, number_of_kills):

        super().__init__(isMammal=True, feet_number=4, )
        self.age = age
        self.skin_color = skin_color
        self.isMale = isMale
        self.number_of_kills = number_of_kills

    def talk(self):
        return "gar gar " + self.emilbek

