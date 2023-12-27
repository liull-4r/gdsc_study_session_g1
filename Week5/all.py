class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Display information about the car
my_car.display_info()

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

    def charge_battery(self):
        print("Charging the battery...")

    def drive(self, distance):
        if distance <= self.calculate_range():
            print(f"The car drives {distance} miles.")
            self.battery_capacity -= distance / 10
        else:
            print("Not enough charge to drive that far.")

    def calculate_range(self):
        return self.battery_capacity * 10

# Create an instance of ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 2023, 75)

# Display information about the electric car
my_electric_car.display_info()

# Charge the battery
my_electric_car.charge_battery()

# Drive the electric car
my_electric_car.drive(50)

# Display updated information after driving
my_electric_car.display_info()

class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrawn {amount}. New balance: {self._balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Current balance: {self._balance}")


# Create an instance of BankAccount
my_account = BankAccount()

# Deposit money
my_account.deposit(100)

# Withdraw money
my_account.withdraw(50)

# Display balance
my_account.display_balance()

import math

class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


# Create instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Calculate and display the areas of different shapes
print("Area of the circle:", circle.calculate_area())
print("Area of the rectangle:", rectangle.calculate_area())
print("Area of the triangle:", triangle.calculate_area())

import unittest

class BankAccountTests(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()

    def test_initial_balance(self):
        self.assertEqual(self.account._balance, 0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account._balance, 100)

    def test_invalid_deposit(self):
        self.account.deposit(-50)
        self.assertEqual(self.account._balance, 0)

    def test_withdraw_sufficient_funds(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.assertEqual(self.account._balance, 100)

    def test_withdraw_insufficient_funds(self):
        self.account.withdraw(50)
        self.assertEqual(self.account._balance, 0)

    def test_invalid_withdrawal(self):
        self.account.withdraw(-20)
        self.assertEqual(self.account._balance, 0)

    def test_display_balance(self):
        self.account.deposit(300)
        self.assertEqual(self.account._balance, 300)
        self.assertOutput("Current balance: 300\n", self.account.display_balance)

    def assertOutput(self, expected_output, function):
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with redirect_stdout(f):
            function()
        self.assertEqual(f.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()