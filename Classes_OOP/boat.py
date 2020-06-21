from vehicle import Vehicle

class Boat(Vehicle):
    '''
    Boat models a waterborne vehicle.
    It inherits from the Vehicle class.

    >>> b = Boat()
    >>> b.description()
    'A Boat that has traveled 0 miles using a sail'
    '''
    def __init__(self, boat_type='sail', distance_traveled=0, unit='miles', **kwargs):
        '''
        Initializer for Boat class includes boat type w/ a default
        '''
        super().__init__(distance_traveled=distance_traveled, unit=unit, **kwargs)
        self.boat_type = boat_type

    def description(self):
        '''
        Provides a string description of the car
        '''
        initial = super().description()
        return f"{initial} using a {self.boat_type}"

    def voyage(self, distance):
        '''
        Advances the distance traveled by the boat
        '''
        self.distance_traveled += distance

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    b = Boat()
    print(b.description())
    print(b)