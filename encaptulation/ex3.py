class car:
    def __init__(self, make, model,year):
        self.make = make
        self.model =model
        self.year= year
        self.__reading = 0
    def get_reading(self):
        return self.__reading
    def set_reading(self , mileage):
        if mileage >= self.__reading:
            self.__reading = mileage
        else:
            print("you can't roll back")
    def increment(self,miles):
        if miles>=0:
            self.__reading += miles
        else:
            print("You can't decrement odometer!")
my_car = car("volvo","carmy" ,1970)

print(my_car.make)
print(my_car.model)
print(my_car.year)

print(my_car.get_reading())

my_car.set_reading(7000)

my_car.increment(700)

print(my_car.get_reading())



