"""
 Task 3:
    Write a function that accepts a person's name as a parameter
    and prints a greeting message like: "Hello, John!"
"""

def greet(name):
    return f"hello {name}"

name = input("enter your name: ")

print(greet(name))
