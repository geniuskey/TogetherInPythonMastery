class Target:
    def request(self):
        pass


class Adaptee:
    def specific_request(self):
        print("Specific request")


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()


adaptee = Adaptee()
adapter = Adapter(adaptee)
adapter.request()  # Specific request
