#!/usr/bin/env python3.6
import abc


class Vehicle(metaclass=abc.ABCMeta):
    """Abstract class for vehicles.
    Instance attributes:
        name (str): the name of the vehicle.
        mileage (int): mileage in kilometres.
        year (int): year of manufacture.
        model (str): the model of the vehicle.
        base_price (int or float): base price.

    Methods:
        vehicle_type.
        is_motorcycle.
        purchase_price.
    """
    @property
    def name(self):
        """Checks that it is a str."""
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str), 'Name should be str.'
        self._name = value

    @property
    def mileage(self):
        """Checks that it is a non negative numeric."""
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        assert isinstance(value, (int, float)) and value >= 0, 'Mileage should be numeric >= 0.'
        self._mileage = value

    @property
    def year(self):
        """Checks that it is int in range 1800..2018."""
        return self._year

    @year.setter
    def year(self, value):
        assert isinstance(value, int) and 1800 <= value <= 2018, 'Year should be int in ranges 1800..2018.'
        self._year = value

    @property
    def model(self):
        """Checks that it is a str."""
        return self._model

    @model.setter
    def model(self, value):
        assert isinstance(value, str), 'Model should be str.'
        self._model = value

    @property
    def base_price(self):
        """Checks that it is non negative numeric."""
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        assert isinstance(value, (int, float)) and value >= 0, 'Price should be numeric >= 0.'
        self._base_price = value

    def __init__(self, name, mileage, year, model, base_price):
        self.name = name
        self.mileage = mileage
        self.year = year
        self.model = model
        self.base_price = base_price

    @staticmethod
    @abc.abstractmethod
    def vehicle_type(self):
        """Returns the type of the vehicle."""
        pass

    @classmethod
    def is_motorcycle(cls):
        """Return True if vehicle is a motorcycle, False otherwise."""
        return cls.number_of_cycles < 4

    def purchase_price(self):
        """Calculates price according to the mileage."""
        return self.base_price - 0.1 * self.mileage


class Car(Vehicle):
    """Stands for the car.

    Class attributes:
        number_of_cycles (int) : number of cycles.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not hasattr(self.__class__, 'number_of_cycles'):
            self.__class__.number_of_cycles = 4

    @staticmethod
    def vehicle_type():
        return 'Car'


class Motorcycle(Vehicle):
    """Stands for the motorcycle.

    Class attributes:
        number_of_cycles (int) : number of cycles.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not hasattr(self.__class__, 'number_of_cycles'):
            self.__class__.number_of_cycles = 2

    @staticmethod
    def vehicle_type():
        return 'Motorcycle'


class Truck(Vehicle):
    """Stands for the truck.

    Class attributes:
        number_of_cycles (int) : number of cycles.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not hasattr(self.__class__, 'number_of_cycles'):
            self.__class__.number_of_cycles = 10

    @staticmethod
    def vehicle_type():
        return 'Truck'


class Bus(Vehicle):
    """Stads for the bus.

    Class attributes:
        number_of_cycles (int) : number of cycles.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not hasattr(self.__class__, 'number_of_cycles'):
            self.__class__.number_of_cycles = 6

    @staticmethod
    def vehicle_type():
        return 'Bus'


if __name__ == '__main__':
    car = Car(name='1654613',
              mileage=8000,
              year=1999,
              model='red',
              base_price=500_000)
    print(car.vehicle_type())
    print(car.is_motorcycle())
    print(car.purchase_price())
    moto = Motorcycle(name='151651',
                      mileage=100,
                      year=2017,
                      model='black',
                      base_price=50_000)
    print(moto.vehicle_type())
    print(moto.is_motorcycle())
    print(moto.purchase_price())
    print(moto.year)
    print(moto.model)
    print(moto.base_price)
