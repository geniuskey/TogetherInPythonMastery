class Subject:
    def request(self):
        pass


class RealSubject(Subject):
    def request(self):
        print("RealSubject request")


class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy handling request")
        self._real_subject.request()


real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()
