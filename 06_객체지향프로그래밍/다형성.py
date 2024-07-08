class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


def make_animal_speak(animal):
    print(animal.speak())


# 서로 다른 객체를 동일한 함수로 처리
dog = Dog("Buddy")
cat = Cat("Whiskers")
make_animal_speak(dog)  # Buddy says Woof!
make_animal_speak(cat)  # Whiskers says Meow!
