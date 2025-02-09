# 구조 패턴 (Structural Patterns) - Composite Pattern
class Component:
    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        print("Leaf operation")


class Composite(Component):
    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def operation(self):
        print("Composite operation")
        for child in self._children:
            child.operation()


leaf1 = Leaf()
leaf2 = Leaf()
composite = Composite()
composite.add(leaf1)
composite.add(leaf2)
composite.operation()
