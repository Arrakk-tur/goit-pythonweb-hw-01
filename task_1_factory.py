from abc import ABC, abstractmethod
from typing import Protocol

from own_logger import my_logger


# 1. Абстрактний базовий клас Vehicle
class Vehicle(ABC):
    def __init__(self, make: str, model: str, region_spec: str) -> None:
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


# 2. Класи Car і Motorcycle, що наслідують Vehicle
class Car(Vehicle):
    def start_engine(self) -> None:
        my_logger.info(f"{self.make} {self.model} ({self.region_spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        my_logger.info(f"{self.make} {self.model} ({self.region_spec}): Мотор заведено")


# 3. Протокол для VehicleFactory (альтернатива абстрактному класу з кращою підтримкою типів)
class VehicleFactory(Protocol):
    def create_car(self, make: str, model: str) -> Vehicle: ...

    def create_motorcycle(self, make: str, model: str) -> Vehicle: ...


# 4. Конкретні фабрики US і EU
class USVehicleFactory:
    us_region_spec = "US Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, self.us_region_spec)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, self.us_region_spec)


class EUVehicleFactory:
    eu_region_spec = "EU Spec"

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, self.eu_region_spec)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
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
