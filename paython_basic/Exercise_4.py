"""
    Exercise 4: Concatenate two lists in the following order
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    Expected output:

    ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [i + j for i,j in zip(list1,list2)]
print(res)

res1 = [i + j for i in list1 for j in list2]

print(res1)