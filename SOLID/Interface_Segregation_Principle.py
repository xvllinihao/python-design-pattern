from abc import ABC, abstractmethod

class Walker(ABC):
    @abstractmethod
    def walk(self) :
        print("Can walk")

class Swimmer(ABC):
    @abstractmethod
    def swim(self) :
        print("Can swim")

class Human(Walker, Swimmer):
    def walk(self) :
        print(f"{self.__class__.__name__} can walk")

    def swim(self) :
        print(f"{self.__class__.__name__} can swim")

class Whale(Swimmer):
    def swim(self) :
        print(f"{self.__class__.__name__} can swim")

if __name__ == '__main__':
    human = Human()
    human.swim()
    human.walk()

    whale = Whale()
    whale.swim()