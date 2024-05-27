class enc:
    def __init__(self):
        self.a = "kinal"
        self.c = "ramani"
class kn(enc):
    def __init__(self):
        enc.__init__(self)
        print("calling positive number:-")
        print(self.c)
obj = enc()
obj1= kn()
#print(obj1.c)
print(obj.a)