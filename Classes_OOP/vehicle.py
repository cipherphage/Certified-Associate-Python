class Vehicle:
    '''
    Vehicle models a vehicle w/ distance_traveled and unit
    '''
    def __init__(self, distance_traveled=0, unit='miles'):
        '''
        Initializer for Vehicle class includes distance_traveled
        and unit
        '''
        self.distance_traveled = distance_traveled
        self.unit = unit

    @classmethod
    def bicycle(cls, tires=None):
        '''
        Provides a bicycle class method
        '''
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)

    def description(self):
        '''
        Provides a string description of the vehicle
        '''
        return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}"