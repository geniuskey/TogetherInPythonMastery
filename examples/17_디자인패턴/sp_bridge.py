# 구조 패턴 (Structural Patterns) - Builder Pattern
class Implementation:
    def operation_impl(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation_impl(self):
        print("ConcreteImplementationA operation")


class ConcreteImplementationB(Implementation):
    def operation_impl(self):
        print("ConcreteImplementationB operation")


class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def operation(self):
        self._implementation.operation_impl()


abstraction_a = Abstraction(ConcreteImplementationA())
abstraction_a.operation()  # ConcreteImplementationA operation

abstraction_b = Abstraction(ConcreteImplementationB())
abstraction_b.operation()  # ConcreteImplementationB operation
