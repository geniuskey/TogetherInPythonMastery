class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Product parts:", ", ".join(self.parts))


class Builder:
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

    def get_result(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()


builder = Builder()
director = Director(builder)
director.construct()
product = builder.get_result()
product.show()  # Product parts: Part A, Part B
