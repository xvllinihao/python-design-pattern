# encapsulation means using protected member to store members that cannot be accessed outside the class

class Base:
    def __init__(self):

        # Protected member
        self._a = 2

class Derived(Base):

    def __init__(self):

        # Calling constructor of
        # Base class
        super().__init__()

    def access_a(self):
        print("Calling protected member of base class: ", self._a)


