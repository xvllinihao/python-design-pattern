class Geek:

    # constructor
    def __init__(self, name, age):

        # public data members
        self.geekName = name
        self.geekAge = age

    def displayAge(self):
        print(f"Age: {self.geekAge}")


if __name__ == '__main__':
    obj = Geek("R2J", 20)
    obj.displayAge()
    print(obj.geekAge)