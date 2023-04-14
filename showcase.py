# Name: Showcase
# Author: mos
# Language: EngLang
# Compiled: 2023-04-14
# Compiler: MostlyWhat's EngLang Compiler
# License: wht

SHOWCASE

# Variables
a = 5
b = 2.5
c = "Hello, world!"

# Arithmetic operations
sum = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b

# Comparison operators
x = 10
y = 5
if x GREATER THAN y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")

# Loops
# for loop:
for i IN RANGE(5) DO:
    print(i)

# while loop:
i = 0
while i LESS THAN 5 DO:
    print(i)
    i = i + 1

# LOOP THROUGH LIST
myList = [1, 2, 3, 4, 5]
for item IN myList DO:
    print(item)

# Functions
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
calculator = Calculator()
sum = calculator.add(a, b)
difference = calculator.subtract(a, b)

# Display results
print("a: " + a)
print("b: " + b)
print("c: " + c)
print("sum: " + sum)
print("difference: " + difference)
print("product: " + product)
print("quotient: " + quotient)
print("remainder: " + remainder)
