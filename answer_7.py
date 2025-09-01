"""
    Task 7:
    Write a function that accepts three numbers as parameters
    and returns the largest number.
"""
def find_max(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        return num_1 
    elif num_2 > num_1 and num_2 > num_3:
        return num_2 
    else:
        return num_3 

num_1 = float(input("Enter num_1: "))
num_2 = float(input("Enter num_2: "))
num_3 = float(input("Enter num_3: "))

print(f"the largest number is: {find_max(num_1, num_2, num_3)}")
