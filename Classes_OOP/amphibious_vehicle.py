from boat import Boat
from car import Car

class AmphibiousVehicle(Car, Boat):
    '''
    AmphibiousVehicle models a vehicle w/ both Car and Boat properties.
    It inherits from the Car and Boat classes.

    >>> av = AmphibiousVehicle()
    >>> av.description()
    'A AmphibiousVehicle that has traveled 0 miles using a motor with 4 cylinders and has 4 tires'
    '''
    default_tire = 'tire'

    def __init__(self, engine='4 cylinders', tires=[], distance_traveled=0, unit='miles'):
        '''
        Initializer for AmphibiousVehicle class includes tires w/ a default
        '''
        super().__init__(
            engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit
        )
        if not tires:
            tires = [self.default_tire, self.default_tire, self.default_tire, self.default_tire]
        self.tires = tires
        self.boat_type = 'motor'

    def travel(self, land_distance=0, water_distance=0):
        '''
        Advances the distance traveled by the amphibious vehicle
        '''
        self.voyage(water_distance)
        self.drive(land_distance)

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    av = AmphibiousVehicle()
    print(av.description())

    # use the method resolution order attirbute on our class to
    # see the order in which methods are inherited:
    print(AmphibiousVehicle.__mro__)