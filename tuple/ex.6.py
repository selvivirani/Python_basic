"""
    Exercise 6: Copy specific elements from one tuple to a new tuple
    Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

    Given:

    tuple1 = (11, 22, 33, 44, 55, 66)
    Expected output:

    tuple2: (44, 55)
"""

tp1=(11,77,44,55,97,7)

tp2=tp1[2:-2]

print(tp2)