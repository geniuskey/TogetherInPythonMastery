class Strategy:
    def execute(self, a, b):
        pass


class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)


context = Context(ConcreteStrategyAdd())
print(context.execute_strategy(5, 3))  # 8

context.set_strategy(ConcreteStrategySubtract())
print(context.execute_strategy(5, 3))  # 2
