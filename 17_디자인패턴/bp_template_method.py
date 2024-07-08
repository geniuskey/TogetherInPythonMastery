from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self.operation1()
        self.operation2()

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass


class ConcreteClass(AbstractClass):
    def operation1(self):
        print("Operation 1")

    def operation2(self):
        print("Operation 2")


concrete = ConcreteClass()
concrete.template_method()
