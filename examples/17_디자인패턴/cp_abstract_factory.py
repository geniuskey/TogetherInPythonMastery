# 생성 패턴 (Creational Patterns) - Abstract Factory Pattern
from abc import ABC, abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit_on(self):
        pass


class VictorianChair(Chair):
    def sit_on(self):
        print("Sitting on a Victorian chair")


class ModernChair(Chair):
    def sit_on(self):
        print("Sitting on a Modern chair")


class Sofa(ABC):
    @abstractmethod
    def lie_on(self):
        pass


class VictorianSofa(Sofa):
    def lie_on(self):
        print("Lying on a Victorian sofa")


class ModernSofa(Sofa):
    def lie_on(self):
        print("Lying on a Modern sofa")


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()

    def create_sofa(self):
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()

    def create_sofa(self):
        return ModernSofa()


def client(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    chair.sit_on()
    sofa.lie_on()


client(VictorianFurnitureFactory())  # Victorian furniture
client(ModernFurnitureFactory())  # Modern furniture
