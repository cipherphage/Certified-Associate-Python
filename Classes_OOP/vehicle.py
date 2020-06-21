class Vehicle:
    '''
    Vehicle models a vehicle w/ distance_traveled and unit
    '''
    def __init__(self, distance_traveled=0, unit='miles', **kwargs):
        '''
        Initializer for Vehicle class includes distance_traveled
        and unit

        >>> v = Vehicle()
        >>> v.description()
        'A Vehicle that has traveled 0 miles'
        '''
        self.distance_traveled = distance_traveled
        self.unit = unit

    # This was an example class method we used before creating a 
    # totally separate Bicycle class. This class method no longer works
    # because default_tire is not defined on the Vehicle class anymore.
    #
    # @classmethod
    # def bicycle(cls, tires=None):
    #     '''
    #     Provides a bicycle class method
    #     '''
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)

    def description(self):
        '''
        Provides a string description of the vehicle
        '''
        return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}"

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    v = Vehicle()
    print(v.description())