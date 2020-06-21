from vehicle import Vehicle

class Car(Vehicle):
    '''
    Car models a vehicle w/ tires and an engine.
    It inherits from the Vehicle class.

    >>> c = Car()
    >>> c.description()
    'A Car that has traveled 0 miles with 4 cylinders and has 4 tires'
    '''
    default_tire = 'tire'

    def __init__(self, engine='4 cylinders', tires=[], distance_traveled=0, unit='miles', **kwargs):
        '''
        Initializer for Car class includes tires w/ a default
        '''
        super().__init__(distance_traveled=distance_traveled, unit=unit, **kwargs)
        if not tires:
            tires = [self.default_tire, self.default_tire, self.default_tire, self.default_tire]
        self.tires = tires
        self.engine = engine

    def description(self):
        '''
        Provides a string description of the car
        '''
        initial = super().description()
        return f"{initial} with {self.engine} and has {len(self.tires)} tires"

    def drive(self, distance):
        '''
        Advances the distance traveled by the car
        '''
        self.distance_traveled += distance

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    c = Car()
    print(c.description())