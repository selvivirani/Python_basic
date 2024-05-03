def marks(t):
    def inner(b):
        return t + b
    return inner
add = marks(5)
result = add(7)
print(result)