Comment: Writing comments in Python code.
Python

# This is a comment in Python
AI-generated code. Review and use carefully. More info on FAQ.
Print: Printing output to the console.
Python

print("Hello, World!")
AI-generated code. Review and use carefully. More info on FAQ.
Indentation: Understanding the importance of indentation in Python.
Python

if 5 > 2:
  print("Five is greater than two!")
AI-generated code. Review and use carefully. More info on FAQ.
Variables: Declaring and using variables in Python.
Python

x = 5
y = "John"
print(x)
print(y)
AI-generated code. Review and use carefully. More info on FAQ.
Operators: Using operators in Python.
Python

x = 5
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)

- Conditional Statements: Using if/else statements in Python.

# Example 1: Check if a number is positive or negative
x = int(input("Enter a number: "))
if x > 0:
  print("The number is positive")
elif x == 0:
  print("The number is zero")
else:
  print("The number is negative")

# Example 2: Check if a number is even or odd
x = int(input("Enter a number: "))
if x % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

- For Loops: Using for loops in Python.

# Example 1: Print all numbers from 0 to 4
for i in range(5):
  print(i)

# Example 2: Print all elements in a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

- While loops: Using while loops in Python.

# Example 1: Print all numbers from 0 to 4
i = 0
while i < 5:
  print(i)
  i += 1

# Example 2: Print all elements in a list
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
  print(fruits[i])
  i += 1

- User Input: Getting user input in Python.

# Example 1: Get user's name and print a greeting
name = input("What is your name? ")
print("Hello, " + name + "!")

# Example 2: Get user's age and print a message
age = int(input("What is your age? "))
if age >= 18:
  print("You are an adult")
else:
  print("You are not an adult")

- Typecasting: Converting data types in Python.

# Example 1: Convert a string to an integer
x = int("5")
print(x)

# Example 2: Convert a string to a float
y = float("3.14")
print(y)

- Dictionaries: Using dictionaries in Python.

# Example 1: Create a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Example 2: Access a value in a dictionary
x = thisdict["model"]
print(x)

- Lists: Using lists in Python.

# Example 1: Create a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Example 2: Access an element in a list
x = fruits[1]
print(x)

- Tuples: Using tuples in Python.

# Example 1: Create a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)

# Example 2: Access an element in a tuple
x = fruits[1]
print(x)

- Sets: Using sets in Python.

# Example 1: Create a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Example 2: Add an element to a set
fruits.add("orange")
print(fruits)
# Functions and Arguments
def greet(name):
    print(f"Hello, {name}!")

# Args keyword Arguments
def add_numbers(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

# Default Arguments
def multiply_numbers(a, b=1):
    return a * b

# Scope
x = 10
def print_x():
    x = 5
    print(f"x inside function: {x}")
print_x()
print(f"x outside function: {x}")

# Return Statement
def square(x):
    return x * x

# Lambda Expression
double = lambda x: x * 2

# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]

# OOPS concepts
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

# Classes
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# Methods
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} started.")

# Objects
person = Person("Alice", 25)
dog = Dog("Buddy", "Golden Retriever")
car = Car("Toyota", "Camry")

greet("John")
print(add_numbers(1, 2, 3))
print(multiply_numbers(5))
print(multiply_numbers(5, 3))
print(square(5))
print(double(5))
print(squares)
person.introduce()
dog.bark()
car.start()
# Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instance attribute
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Class attribute
class Car:
    wheels = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Self
class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} says meow!")

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Super
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# Multiple Inheritance
class A:
    def do_something(self):
        print("Method defined in A")

class B(A):
    def do_something(self):
        print("Method defined in B")

class C(A):
    def do_something(self):
        print("Method defined in C")

class D(B, C):
    pass

# Polymorphism
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Encapsulation
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def get_balance(self):
        return self.balance

# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Exceptions
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("Error:", e)

# Package Import
import math
print(math.sqrt(16))

# JSON Handling
import json
person = {"name": "Alice", "age": 25}
person_json = json.dumps(person)
print(person_json)


