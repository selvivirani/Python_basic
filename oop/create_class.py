"""
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.=
"""

class bike:
    def __init__(self,model,price) :
        self.model = model
        self.price = price
mx = bike("audi",30)
print(mx.model , mx.price) 