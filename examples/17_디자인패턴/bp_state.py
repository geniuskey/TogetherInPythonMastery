# 행위 패턴 (Behavioral Patterns) - State Pattern
from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass


class ConcreteStateA(State):
    def handle(self, context):
        print("State A")
        context.state = ConcreteStateB()


class ConcreteStateB(State):
    def handle(self, context):
        print("State B")
        context.state = ConcreteStateA()


class Context:
    def __init__(self, state):
        self.state = state

    def request(self):
        self.state.handle(self)


context = Context(ConcreteStateA())
context.request()  # State A
context.request()  # State B
