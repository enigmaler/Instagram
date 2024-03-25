from animal import Mammal
class Dog(Mammal):

    def __init__(self, breed, color, sex, age, speed, name):
        super().__init__(sex=sex, age=age, speed=speed, name=name)

        self.breed = breed
        self.color = color

    def voice(self):
        return f"This is voice of {self.breed}"

    def speedy(self):
        return f"can run at {self.speed} m/h"

    def parent_speedy(self):
        return f"can run at {super().speedy()} m/h"

    def get_sex(self):
        return self.sex

    def set_sex(self, curr_sex):

        self.sex = curr_sex
        return self.sex


    def dreams(self):
        return super().dreams() + "meats"

dog1 = Dog("Shepherd", "Black", "male", 6, 10, "sharik")

print(dog1.breed)
print(dog1.voice())


print(f"This dog's breed is {dog1.breed}. It's sex is {dog1.sex}. It {dog1.parent_speedy()}")

print(dog1.parent_speedy())

print(dog1.sex)
print(dog1.set_sex("transgender"))
print(dog1.get_sex())

print(dog1.dreams())

