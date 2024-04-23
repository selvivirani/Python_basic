"""
    Exercise 5: Create an inner function to calculate the addition in the following way

    AD
    Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate the addition of a and b
    At last, an outer function will add 5 into addition and return it
"""
def outer(a,b):
    def addtion(a,b):
        return a + b

    add = addtion(a,b)
    return add + 5


# addtion = (5, 6)
result = outer(5, 10)
print(result)