class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False


# 객체 생성 및 메소드 호출
person = Person("Alice", 30)
print(person)  # Alice, 30
print(repr(person))  # Person(name='Alice', age=30)

person2 = Person("Alice", 30)
print(person == person2)  # True


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# 객체 생성 및 메소드 호출
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Vector(6, 8)