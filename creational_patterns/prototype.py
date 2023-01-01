"""
Prototype allows user to clone the object
"""
import copy


class SomeComponent:

    def __init__(self, some_int, some_list, some_ref):
        self.some_int = some_int
        self.some_list = some_list
        self.some_ref = some_ref

    def __copy__(self):

        some_list = copy.copy(self.some_list)
        some_ref = copy.copy(self.some_ref)

        new = self.__class__(
            self.some_int, some_list, some_ref
        )

        return new

    def __deepcopy__(self, memodict={}):

        some_list = copy.deepcopy(self.some_list)
        some_ref = copy.deepcopy(self.some_ref)

        new = self.__class__(
            self.some_int, some_list, some_ref
        )

        new.__dict__ = copy.deepcopy(self.__dict__, memodict)

        return new