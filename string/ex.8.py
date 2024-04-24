"""
    Exercise 9: Calculate the sum and average of the digits present in a string
    Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

    Given:

    str1 = "PYnative29@#8496"
    Expected Outcome:

    Sum is: 38 Average is  6.333333333333333
"""
str1 = "PYnative29@#8496"

digit = 0
sum = 0

for char in str1:
    if char.isdigit():
        sum += int(char)
        digit += 1

avg = sum/digit
print(f"sum is {sum} average is {avg}")