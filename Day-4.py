# Q1
class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return 'Successful Process'

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            return 'Successful Process'
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance


obj = BankAccount("Seif", 2000)
obj.deposit(500)
print("After Deposit",obj.get_balance())
obj.withdraw(100)
print("After Withdraw",obj.get_balance())

# Q2 ---------------------------------------------------------------------------------
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

    def is_square(self):
        return True if self.width == self.length else False

obj = Rectangle(5,5)
print("Area:-",obj.calculate_area())
print("perimeter:-",obj.calculate_perimeter())
print("Is_square:-",obj.is_square())

# Q3 ---------------------------------------------------------------------------------

class Temperature:
    def __init__(self,temp):
        self.temp = temp

    def convert_to_fahrenheit(self):
        return  self.temp * 9/5 + 32

    def convert_to_kelvin(self):
        return self.temp + 273.15

obj = Temperature(25)
print(obj.convert_to_fahrenheit())
print(obj.convert_to_kelvin())

# Q4 ---------------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary, job_title):
        super().__init__(name, age)
        self.salary = salary
        self.job_title = job_title

    def give_raise(self, percentage):
        self.salary += (self.salary * percentage) / 100
        return self.salary


obj = Employee("Ahmed", 30, 5000, "Engineer")
print(obj.give_raise(10))

# Q5 ---------------------------------------------------------------------------------

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 29


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def calculate_area(shape):
    return shape.area()


print(calculate_area(Circle(5)))
print(calculate_area(Rectangle(4, 5)))

# Q6 ---------------------------------------------------------------------------------

class MathOperations:
    def __init__(self):
        pass

    def calculate(self, *numbers):
        sum = 0
        for i in numbers:
            sum += i
        return sum
        ## return sum(numbers)        ### using bult in method

obj = MathOperations()
print(obj.calculate(10,5))
print(obj.calculate(10,5,15))

# Q7 ---------------------------------------------------------------------------------

class PasswordManager:
    def __init__(self):
        self.__password = 0

    def set_password(self,password):
        if len(password) >= 8:
            self.__password = password
            return 'Password set'
        else:
            return 'Password too short'

    def verify(self,verify_password):
        return True if self.__password == verify_password else False

obj = PasswordManager()
print(obj.set_password("abc"))
print(obj.set_password("secure123"))
print(obj.verify("secure123"))

# Q8 ---------------------------------------------------------------------------------

class PasswordManager:
    def __init__(self):
        self.__password = 0

    def set_password(self,password):
        if len(password) <= 8:
            self.__password = password
            return 'Password set'
        else:
            return 'Password too short'

    def verify(self,input_password):
        return True if self.__password == input_password else False

# Q9 ---------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return 'This is a shape'


class Circle(Shape):
    def __init__(self,r):
        self.r = r
        super().__init__()

    def area(self):
        return 3.14 * self.r * self.r

obj = Circle(10)
print(obj.area())

# Q10 ---------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    def __init__(self,salary):
        self.salary = salary
    @property
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def __init__(self,salary):
        super().__init__(salary)

    def calculate_bonus(self):
        return (self.salary * 20) / 100


class Developer(Employee):
    def __init__(self, salary):
        super().__init__(salary)

    def calculate_bonus(self):
        return (self.salary * 10) / 100

print(Manager(salary=10000).calculate_bonus())
print(Developer(salary=8000).calculate_bonus())