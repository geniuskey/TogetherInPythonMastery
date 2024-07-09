class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation")


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        print("ConcreteDecoratorA operation")
        super().operation()


class ConcreteDecoratorB(Decorator):
    def operation(self):
        print("ConcreteDecoratorB operation")
        super().operation()


component = ConcreteComponent()
decorator_a = ConcreteDecoratorA(component)
decorator_b = ConcreteDecoratorB(decorator_a)
decorator_b.operation()
