from abc import ABC, abstractmethod
class Mammal(ABC):

    def __init__(self, sex, age, name, speed, can_fly= False, can_swim=False):
        self.sex = sex
        self.can_swim = can_swim
        self.can_fly = can_fly
        self.age = age
        self.name = name
        self.speed = speed


    def voice(self):
        return "voice"

    def speedy(self):
        return f"{self.speed}"

    @abstractmethod
    def dreams(self):
        return "Dreams about "



