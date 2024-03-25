from abc import ABC, abstractmethod
from AbsOfAnimal import Abs_Animal

class Animal():


    def __init__(self, age =3, isMammal = False, isMale = None, feet_number = 0, skin_color= None):

        self.age = age;
        self.isMammal = isMammal;
        self.isMale = isMale
        self.feet_number = feet_number
        self.skin_color = skin_color

    def can_sleep(self):
        return "f"

    def talk(self):
        return "gaf gaf"

def c(t):
    return 3