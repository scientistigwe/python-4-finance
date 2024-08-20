# Basic syntax
# 1. Variables: works on the concept of name binding.
# Everything in python is an object. 3 core parts of an object: identifier/reference, type, value.

# OOP Concepts: 1. Encapsulation: Bundling of data and methods that operate on that data within a single unit.
# In this example, __balance is a private attribute that can only be accessed within the class

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100 * 2)
print(account.get_balance())


# 2. Inheritance: Class can inherit methods and attributes from another class

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return (f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        return (f"{self.name} says Meow!")

dog = Dog('Buddy')
cat = Cat('Whisker')

print(dog.speak())
print(cat.speak())