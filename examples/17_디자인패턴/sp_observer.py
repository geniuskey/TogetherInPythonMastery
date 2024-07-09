# 구조 패턴 (Structural Patterns) - Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()


class Observer:
    def update(self):
        pass


class ConcreteObserver(Observer):
    def update(self):
        print("Observer notified")


subject = Subject()
observer = ConcreteObserver()
subject.add_observer(observer)
subject.notify_observers()
