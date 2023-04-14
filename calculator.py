# Name: Calculator
# Author: mos
# Language: EngLang
# Compiled: 2023-04-14
# Compiler: MostlyWhat's EngLang Compiler
# License: wht

CALCULATOR
class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
x = 5
y = 3

if x IS GREATER THAN y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")

calculator = Calculator()
sum = calculator.add(x, y)
difference = calculator.subtract(x, y)

print("The sum is " + str(sum))
print("The difference is " + str(difference))
