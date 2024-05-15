class public:
    def __init__(self, number):
        self.number = number
        #self.name = name
    def __len__(self):
        return self.number
obj = public(12)
#obj2 = public("henny")
print(len(obj))
#print(len(obj2))