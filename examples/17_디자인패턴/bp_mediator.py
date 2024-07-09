from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self.component1 = component1
        self.component1.set_mediator(self)
        self.component2 = component2
        self.component2.set_mediator(self)

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self.component2.do_c()
        if event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self.component1.do_b()


class BaseComponent:
    def __init__(self):
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator


class Component1(BaseComponent):
    def do_a(self):
        print("Component 1 does A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Component 1 does B.")


class Component2(BaseComponent):
    def do_c(self):
        print("Component 2 does C.")

    def do_d(self):
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


component1 = Component1()
component2 = Component2()
mediator = ConcreteMediator(component1, component2)

component1.do_a()
component2.do_d()
