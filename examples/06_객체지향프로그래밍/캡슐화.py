class Person:
    def __init__(self, name, age):
        self.__name = name  # private 변수
        self.__age = age  # private 변수

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 120:  # 간단한 유효성 검사
            self.__age = age
        else:
            raise ValueError("Invalid age")


# 객체 생성 및 메소드 호출
person = Person("Alice", 30)
print(person.get_name())  # Alice
print(person.get_age())  # 30

person.set_name("Bob")
person.set_age(25)
print(person.get_name())  # Bob
print(person.get_age())  # 25

# 직접 접근 시도 (실패)
# print(person.__name)  # AttributeError: 'Person' object has no attribute '__name'
