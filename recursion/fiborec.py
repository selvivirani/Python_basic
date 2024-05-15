def fibo(n):
    if n <= 1:
        return n 
    else:
        return(fibo (n-1) + fibo (n-2))
n_tem = 10

if n_tem <= 1:
    print("Invalid input! please enter positive number")
else:
    print("fibonaki serice:")
for i in range(n_tem):
    print(fibo(i))