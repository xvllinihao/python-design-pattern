import numpy as np
from abc import ABC, abstractmethod

class Operation(ABC):
    """Operation"""
    @abstractmethod
    def operation(self, _list):
        pass

class Mean(Operation):
    def operation(self, _list):
        print(f"the mean of the list is {np.mean(_list)}")

class Max(Operation):
    def operation(self, _list):
        print(f"the max of the list is {np.max(_list)}")


class Main:
    @abstractmethod
    def get_operations(self, list_):
        for operation in Operation.__subclasses__():
            op = operation()
            op.operation(list_)

if __name__ == '__main__':
    main = Main()
    main.get_operations([1,2,3,4,5])