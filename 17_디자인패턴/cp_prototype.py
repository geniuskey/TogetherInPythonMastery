import copy


class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)


prototype1 = Prototype(10)
prototype2 = prototype1.clone()
print(prototype1.value, prototype2.value)  # 10 10

prototype2.value = 20
print(prototype1.value, prototype2.value)  # 10 20
