class Employee:
    company = "ITC"  # Added as a class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):  # Inheriting from Employee
    company = "ITC Inc"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)  # Initialize name and salary from parent class
        self.language = language

    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")

a = Employee("John", 50000)
b = Programmer("Jane", 60000, "Python")

print(a.company, b.company)
