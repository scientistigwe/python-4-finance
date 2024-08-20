# Basic syntax
# 1. Variables: works on the concept of name binding.
# Everything in python is an object. 3 core parts of an object: identifier/reference, type, value.
from mailcap import subst

from PIL.ImageChops import subtract


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

# Control Flow: The order a statement/function/instruction is executed
# 1. IF, ELIF, ELSE: executed if the condition is met
x = 8

if x > 10:
    print("X is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("X is less than 10")

# 2. Match: executed based on pattern matching
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 409:
            return "Multiple request"
        case 500:
            return "Server Error"
        case _:
            return "Unknown status code"

print(f"Http status for code 500 is '{http_status(500)}'")

def calculator():
    try:
        input_string = input("Enter num1, num2 separated by ',': ")
        num1, num2 = input_string.split(',')
        num1 = int(num1)
        num2 = int(num2)
        numbers = [num1, num2]
        print(f'{num1}, {num2}')

        add_num = sum(numbers)
        subst_num = num1 - num2
        print(f"{add_num}, {subst_num}")
    except ValueError as e:
        if e:
            print(f"Error: {e}")
    finally:
        print("Thank you for trying me out")

answer = calculator()
print(answer)

def divide(a,b):
    import pdb; pdb.set_trace()
    return a/b

divide(10,0)



