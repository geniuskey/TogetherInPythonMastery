# 생성 패턴 (Creational Patterns) - Factory method Pattern
from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def use(self):
        pass


class ConcreteProductA(Product):
    def use(self):
        print("Using Product A")


class ConcreteProductB(Product):
    def use(self):
        print("Using Product B")


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def create_product(self):
        product = self.factory_method()
        product.use()


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


creator_a = ConcreteCreatorA()
creator_a.create_product()  # Using Product A
