class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age
        else:
            raise ValueError("Invalid age")


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id


# 객체 생성 및 메소드 호출
employee = Employee("Charlie", 35, "E12345")
print(employee.get_name())  # Charlie
print(employee.get_age())  # 35
print(employee.get_employee_id())  # E12345
