class Geek:

    # private members
    __name = None
    __roll = None
    __branch = None

    # constructor
    def  __init__(self, name, roll, branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    def __displayDetails(self):

        # accessing private data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    def accessPrivateFunction(self):
        self.__displayDetails()

if __name__ == '__main__':
    # creating objects
    obj = Geek("R2J", 1706256, "Information Technology")

    # calling public member function of the class
    obj.accessPrivateFunction()
