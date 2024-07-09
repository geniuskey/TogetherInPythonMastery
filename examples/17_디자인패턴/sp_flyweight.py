# 구조 패턴 (Structural Patterns) - Flyweight Pattern
class Flyweight:
    def __init__(self, intrinsic_state):
        self._intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        print(f"Intrinsic state: {self._intrinsic_state}, Extrinsic state: {extrinsic_state}")


class FlyweightFactory:
    _flyweights = {}

    @staticmethod
    def get_flyweight(key):
        if key not in FlyweightFactory._flyweights:
            FlyweightFactory._flyweights[key] = Flyweight(key)
        return FlyweightFactory._flyweights[key]


flyweight1 = FlyweightFactory.get_flyweight("state1")
flyweight1.operation("extrinsic1")

flyweight2 = FlyweightFactory.get_flyweight("state1")
flyweight2.operation("extrinsic2")

print(flyweight1 is flyweight2)  # True
