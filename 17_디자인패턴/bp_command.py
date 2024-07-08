from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action()


class Receiver:
    def action(self):
        print("Receiver action")


class Invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command):
        self._commands.append(command)

    def execute_commands(self):
        for command in self._commands:
            command.execute()


receiver = Receiver()
command = ConcreteCommand(receiver)
invoker = Invoker()
invoker.add_command(command)
invoker.execute_commands()
