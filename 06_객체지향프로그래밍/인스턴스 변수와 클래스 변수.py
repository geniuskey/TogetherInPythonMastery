class Person:
    species = "Homo sapiens"  # 클래스 변수

    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self.age = age  # 인스턴스 변수


# 객체 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 클래스 변수 접근
print(person1.species)  # Homo sapiens
print(person2.species)  # Homo sapiens

# 인스턴스 변수 접근
print(person1.name)  # Alice
print(person2.name)  # Bob
