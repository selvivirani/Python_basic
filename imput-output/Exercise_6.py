"""
    Exercise 6: Write all content of a given file into a new file by skipping line number 5
    Create a test.txt file and add the below content to it.
"""

with open('test.txt', 'r') as file:
    lines = file.readlines()

with open('new_file.txt', 'w') as new_file:
    for index, line in enumerate(lines):
        if index != 4:  # Skip line number 5 (index starts from 0)
            new_file.write(line)

print("The contents have been written to new_file.txt successfully.")
