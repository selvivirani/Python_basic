def dec(func):
    def inner(*args , **kwargs):
        print("*" * 7)
        func(*args , **kwargs)
        print("*" * 7)
    return inner

def percent(func):
    def inner(*args , **kwargs):
        print("%" * 7)
        func(*args , **kwargs)
        print("%" * 7)
    return inner 

@ dec
@percent
def printer(msg):
    print(msg)
printer("HELLO")