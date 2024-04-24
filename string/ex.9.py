"""
    Exercise 10: Write a program to count occurrences of all characters within a string
    Given:

    str1 = "Apple"
    Expected Outcome:

    {'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""
str1="lichi"
char_dic=dict()

for char in str1:
    count=str1.count(char)
    char_dic[char]= char
    print(char_dic)