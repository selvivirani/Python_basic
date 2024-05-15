def fect(n):
    if n == 0:
        return 1
    else:
        return n * fect(n-1)
result = fect(5)
print("factorial is:-",result)          

