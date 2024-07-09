from abc import ABC, abstractmethod


class Context:
    def __init__(self, expression):
        self.expression = expression


class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass


class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        print(f"Interpreting terminal expression: {context.expression}")


class NonTerminalExpression(AbstractExpression):
    def __init__(self, expression):
        self.expression = expression

    def interpret(self, context):
        print(f"Interpreting non-terminal expression: {context.expression}")
        self.expression.interpret(context)


context = Context("Hello")
terminal_expression = TerminalExpression()
non_terminal_expression = NonTerminalExpression(terminal_expression)

non_terminal_expression.interpret(context)
