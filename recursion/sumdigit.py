def sum(n):
    if n < 10 :
        return n
    else:
        return n % 10 + sum(n // 10)
num = 12345
print("sum of digit:-",num ,"is", sum(num))