class SubsystemA:
    def operation_a(self):
        print("SubsystemA operation")


class SubsystemB:
    def operation_b(self):
        print("SubsystemB operation")


class Facade:
    def __init__(self):
        self._subsystem_a = SubsystemA()
        self._subsystem_b = SubsystemB()

    def operation(self):
        self._subsystem_a.operation_a()
        self._subsystem_b.operation_b()


facade = Facade()
facade.operation()
