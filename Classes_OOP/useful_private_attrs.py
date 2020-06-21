
# __bases__, __subclasses__, dir()
#
# $ python3.7 -i amphibious_vehicle.py
# >>> AmphibiousVehicle.__bases__
# (<class 'car.Car'>, <class 'boat.Boat'>)
# >>> from vehicle import Vehicle
# >>> Vehicle.__subclasses__()
# [<class 'boat.Boat'>, <class 'car.Car'>]
# >>> dir(AmphibiousVehicle)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'default_tire', 'description', 'drive', 'travel', 'voyage']


# hasattr()
#
# >>> from boat import Boat
# >>> hasattr(Boat, 'boat_type')
# False
# >>> from car import Car
# >>> hasattr(Car, 'default_tire')
# True


# issubclass()
#
# >>> from vehicle import Vehicle
# >>> issubclass(Boat, Vehicle)
# True
# >>> issubclass(Boat, AmphibiousVehicle)
# False
# >>> issubclass(AmphibiousVehicle, Boat)
# True


# isinstance()
#
# >>> from bicycle import Bicycle
# >>> water_car = AmphibiousVehicle('4 cylinder')
# >>> isinstance(water_car, Bicycle)
# False
# >>> isinstance(water_car, AmphibiousVehicle)
# True
# >>> isinstance(water_car, Boat)
# True


# __dict__
#
# >>> water_car.__dict__
# {'distance_traveled': 0, 'unit': 'miles', 'boat_type': 'motor', 'tires': ['tire', 'tire'], 'engine': '4 cylinder'}
# >>> Boat.__dict__
# mappingproxy({'__module__': 'boat', '__init__': <function Boat.__init__ at 0x7ff9228b9f80>, 'voyage': <function Boat.voyage at 0x7ff9228b9dd0>, 'description': <function Boat.description at 0x7ff922835050>, '__doc__': None})


# type()
#
# >>> type(water_car)
# <class '__main__.AmphibiousVehicle'>


# __module__
#
# be careful because this one can show 'main' instead of the 
# module name under certain circumstances
# >>> Boat.__module__
# 'boat'


