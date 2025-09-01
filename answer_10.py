"""
    Task 10:
    Write a function that accepts a list of numbers as a parameter
    and returns the product of all the numbers in the list.
    Example: multiply_list([1, 2, 3, 4]) → 24
"""

def multiply_list(numbers):
    product = 1
    for i in numbers:
        product *= i 
    return product


print(multiply_list([1, 2, 3, 4]))
