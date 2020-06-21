from vehicle import Vehicle

class Bicycle(Vehicle):
    '''
    Bicycle models a vehicle w/ tires and no engine.
    It inherits from the Vehicle class.

    >>> b = Bicycle()
    >>> b.description()
    'A Bicycle that has traveled 0 miles on 2 tires'
    '''
    default_tire = 'tire'

    def __init__(self, tires=[], distance_traveled=0, unit='miles'):
        '''
        Initializer for Bicycle class includes tires w/ a default
        '''
        super().__init__(distance_traveled, unit)
        if not tires:
            tires = [self.default_tire, self.default_tire]
        self.tires = tires

    def description(self):
        '''
        Provides a string description of the bicycle
        '''
        initial = super().description()
        return f"{initial} on {len(self.tires)} tires"

    def pedal(self, distance):
        '''
        Advances the distance traveled by the bicycle
        '''
        self.distance_traveled += distance

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    b = Bicycle()
    print(b.description())