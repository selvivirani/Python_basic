"""
OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
"""

class car:
    def __init__(self, name,speed,price):
        self.name = name
        self.speed = speed
        self.price = price

class bus(car):
        pass
sb = bus ("volvo" , 170 , 1800000)
print("car name:" ,sb.name , "car speed:",sb.speed ,"car price:", sb.price)

        