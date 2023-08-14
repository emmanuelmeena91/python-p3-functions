#!/usr/bin/env python3

def greet_programmer():
    print("Hello programmer")

def greet(name):
    print("Hello," + name)

def greet_with_default(name="programmer"):
    print("Hello," + name)

def add(num1, num2):
    return num1 + num2 
sum = add(2 , 3)
 


def halve(number):
    if not isinstance(number, (int, float)):
        return 'halve two'
    return number/ 2
result = halve(4)
result = halve("not NO")


greet_programmer()

greet("Naureen!")

greet_with_default("Sunny!")
greet_with_default()

print(sum)   

print(result)

