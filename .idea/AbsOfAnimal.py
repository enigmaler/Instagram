from abc import ABC, abstractmethod

class Abs_Animal(ABC):

    @abstractmethod
    def can_sleep(self):
        pass