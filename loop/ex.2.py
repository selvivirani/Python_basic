"""
    Exercise 2: Print the following pattern
    Write a program to print the following number pattern using a loop.

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
"""
num = 5
for i in range(1, num + 1):
    for k in range(1, i + 1):
        print(k, end='')
    print()