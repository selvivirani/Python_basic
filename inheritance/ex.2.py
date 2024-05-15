class person:
    def __init__(self,name,age):
        self.name = name
        self.age =  age
    def display(self):
         print(self.name, self.age)
class emp(person):
        def __init__(self, name, age):
             self.name = name
             self.age = age
             super().__init__("ruaan", age)
             #self.emp_id = emp_id
        def pri(self):
             print("emp class called")
emp_det = emp("ruaan", 77)
#emp_det.emp()
emp_det.pri()
emp_det.display()
#emp_det.person()


