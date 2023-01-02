from abc import ABC, abstractmethod


class Country(ABC):
    _captial  = None
    _language = None
    _type = None

    @abstractmethod
    def capital(self):
        pass

    @abstractmethod
    def language(self):
        pass

    @abstractmethod
    def type(self):
        pass

class India(Country):
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language of India")

    def type(self):
        print("India is a developing country.")

class USA(Country):
    def capital(self):
        print("Washington, D.C. is the capital of USA")

    def language(self):
        print("English")

    def type(self):
        print("USA is a developed country.")
def country_information(country: Country):
    country.capital()
    country.language()
    country.type()

if __name__ == '__main__':
    obj_ind = India()
    obj_usa = USA()

    country_information(obj_ind)
    country_information(obj_usa)