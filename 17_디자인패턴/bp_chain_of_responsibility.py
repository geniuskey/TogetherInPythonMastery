from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return f"Handler A handled {request}"
        else:
            return super().handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return f"Handler B handled {request}"
        else:
            return super().handle(request)


handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()

handler_a.set_next(handler_b)

print(handler_a.handle("A"))  # Handler A handled A
print(handler_a.handle("B"))  # Handler B handled B
print(handler_a.handle("C"))  # None
