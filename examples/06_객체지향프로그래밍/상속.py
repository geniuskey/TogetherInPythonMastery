class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # 하위 클래스에서 구현


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# 객체 생성 및 메소드 호출
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name, "says", dog.speak())  # Buddy says Woof!
print(cat.name, "says", cat.speak())  # Whiskers says Meow!
