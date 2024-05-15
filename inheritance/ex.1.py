class inherit(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def disply(self):
        print(self.name,self.id)
emp =  inherit("kinal",23)
emp.disply() 