def decorator(func):
    def add(a , t):
        print("THIS IS SUM ",a , "AND", t)
        if t == 0:
          print("WHOOPA! CANNOT DIVIDE")
          return
        return func(a, t)
    return add
@ decorator
def dec(a , t):
   print(a/t)
dec(5 ,7)
dec(17 , 7)

   
    
    
