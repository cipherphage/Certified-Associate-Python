class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        # by using the private copy of the update method we ensure
        # that only this version of the update method is used, not
        # the version in the subclass below
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

    def print_something(self):
        print("something")

    # this won't work:
    __update = print_something
    # why? because Python performs name mangling:
    # __update in the Mapping class becomes _Mapping__update
    # and __update in the MappingSubclass subclass becomes _MappingSubclass__update

    # creating an identifier that will be name mangled:
    # - The name starts with at least two underscores (_).
    # - The name has at most one trailing underscore (_).
    # - The identifier must be defined in the definition of the class at the same level as methods.