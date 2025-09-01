"""
    Task 13:
    Demonstrate local and global scope.
    Create a global variable, and then inside a function,
    create a local variable with the same name. Print both
    to show how local and global scope works.
"""
global_var = "this is a global variabel outside the function"

def scope_demo():
    global_var = f"this is a local variabel inside the function"
    print(f"inside function: {global_var}")
    print(f"inside function: {global_var}") 

