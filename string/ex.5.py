"""
    Exercise 5: Count all letters, digits, and special symbols from a given string
    Given:

    str1 = "P@#yn26at^&i5ve"
    Expected Outcome:

    Total counts of chars, digits, and symbols

    Chars = 8
    Digits = 3
    Symbol = 4
"""
str1="py@native^$add31"

char_count = 0
digit_count = 0
symbol_count = 0

for char in str1:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1
print(f"char is = {char_count} \ndigit is = {digit_count} \nsymbol is = {symbol_count}")