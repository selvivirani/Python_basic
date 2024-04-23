"""
    Exercise 6: Create a recursive function
    Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

    A recursive function is a function that calls itself again and again.

    Expected Output:

    55
"""


def recursive_func(n):
    if n == 0:
        return 0
    else:
        return n + recursive_func(n - 1)

result = recursive_func(10)
print(result)