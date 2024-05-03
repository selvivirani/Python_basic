def decorator(func):
    def deco():
        print('THIS IS DECORATER')
        func()
    return deco
@ decorator
def dec():
    print('THIS IS NOT DECORATER')
dec()


