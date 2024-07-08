class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# 객체 생성 및 메소드 호출
person = Person("Alice", 30)
person.greet()  # Hello, my name is Alice and I am 30 years old.
