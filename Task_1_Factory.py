from abc import ABC, abstractmethod

# 1. Абстрактний базовий клас Vehicle
class Vehicle(ABC):
    def __init__(self, make, model, region_spec):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self):
        pass

# 2. Класи Car і Motorcycle, що наслідують Vehicle
class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region_spec}): Двигун запущено")

class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model} ({self.region_spec}): Мотор заведено")

# 3. Абстрактна фабрика VehicleFactory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Vehicle:
        pass

# 4. Фабрики US і EU
class USVehicleFactory(VehicleFactory):
    us_region_spec = "US Spec"

    def create_car(self, make, model):
        return Car(make, model, self.us_region_spec)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.us_region_spec)

class EUVehicleFactory(VehicleFactory):
    eu_region_spec = "EU Spec"

    def create_car(self, make, model):
        return Car(make, model, self.eu_region_spec)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.eu_region_spec)


# Використання

# Створення фабрик
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

# Створення транспортних засобів через фабрики
vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")

vehicle1.start_engine()
vehicle2.start_engine()
