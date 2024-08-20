# UNITTEST: Test_Driven Development Principle States that unittest is to be built before building the functionality for that given task.
# Build a simple addition calculator

class Calculator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b


def main(self):
    calc = Calculator()

    # example usage
    print(f"Addition of 5 and 3 is {self.calc.add(5,3)}")
    print(f"Subtraction of 3 from 5 is {self.calc.subtract(5,3)}")

if __name__ == '__main__':
    main()
