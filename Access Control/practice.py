# super class
class Super:

    # public data member
    var1 = None

    #protected data member
    _var2 = None

    #private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    def displayPublicMembers(self):

        # accessing public data members
        print("Public Data Member: ", self.var1)

    def _displayProtectedMembers(self):

        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    def __displayPrivateMembers(self):

        # accessing private data members
        print("Private Data Member: ", self.__var3)

    def accessPrivateMembers(self):

        self.__displayPrivateMembers()

# derived class
class Sub(Super):

    # constructor
    def __init__(self, var1, var2, var3):
        super().__init__(var1, var2, var3)

    # public member function
    def accessProtectedMembers(self):

        # accessing protected member function of super class
        self._displayProtectedMembers()

if __name__ == '__main__':
    obj = Sub("Geeks", 4, "Geeks !")

    # calling public member functions of the class
    obj.displayPublicMembers()
    obj.accessProtectedMembers()
    obj.displayPublicMembers()

    print(f"protected member: {obj._var2}")