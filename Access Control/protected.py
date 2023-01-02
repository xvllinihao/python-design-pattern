# super class
class Student:

    # protected data members
    _name = None
    _roll = None
    _branch = None

    # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    def _displayRollAndBranch(self):

        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)

class Geek(Student):

    # constructor
    def __init__(self, name, roll, branch):
        super().__init__(name, roll, branch)

    def displayDetails(self):
        print("Name", self. _name)
        self._displayRollAndBranch()

if __name__ == '__main__':
    obj = Geek("R2J", 1706265, "Information Technology")
    obj.displayDetails()
