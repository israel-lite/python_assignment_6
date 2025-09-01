"""
    Task 1:
    Write a function that accepts two numbers (a and b) as parameters
    and returns their sum.
    Test the function by calling it with different numbers.
"""

def sum(num_1, num_2):
    return num_1 + num_2

num_1 = int(input("Enter num_1: "))    
num_2 = int(input("Enter num_2: "))

result = sum(num_1, num_2)
print(result)
