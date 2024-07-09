class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def species_info(cls):
        print(f"Species: {cls.species}")


# 클래스 메소드 호출
Person.species_info()  # Species: Homo sapiens
