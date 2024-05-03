"""
    Exercise 5: Swap two tuples in Python
    Given:

    tuple1 = (11, 22)
    tuple2 = (99, 88)

    
    Expected output:

    tuple1: (99, 88)
    tuple2: (11, 22)
"""
tp1=(11,77)
tp2=(47,37)

tp1,tp2=tp2,tp1
print(tp1)
print(tp2)