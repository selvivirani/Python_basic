"""
    Exercise 10: Read line number 4 from the following file
    See:

    Read Specific Lines From a File in Python
        Python read file
    Create a test.txt file and add the below content to it.

    test.txt file
    line1
    line2
    line3
    line4
    line5
    line6
    line7
"""

with open("other.py","r") as fn:
    lines = fn.readlines()

    print(lines[3])