# 클래스 정의
class Person:
    # 생성자 메소드
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self.age = age  # 인스턴스 변수

    # 인스턴스 메소드
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# 객체 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 메소드 호출
person1.greet()  # Hello, my name is Alice and I am 30 years old.
person2.greet()  # Hello, my name is Bob and I am 25 years old.
