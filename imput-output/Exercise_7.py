"""
    Exercise 7: Accept any three string from one input() call
    Write a program to take three names as input from a user in the single input() function call.

    Expected Output

    Enter three string Emma Jessa Kelly
    Name1: Emma
    Name2: Jessa
    Name3: Kelly
"""


str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)