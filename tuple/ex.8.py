"""
    Exercise 8: Sort a tuple of tuples by 2nd item
    Given:

    tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
    Expected output:

    (('c', 11), ('a', 23), ('d', 29), ('b', 37))
"""
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple2= sorted(tuple1,key= lambda x: x[1])
print(tuple(tuple2))

