"""
    Task 8:
    Write a function that accepts a number and returns
    "Even" if the number is even, and "Odd" if the number is odd.
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter number: "))
print(even_or_odd(num))
