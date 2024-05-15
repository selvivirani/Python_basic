num = int(input("enter prime num:-"))
if num > 1:
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i  == 0:
            prime = False
            break
    if prime:
            print("This is prime number",num)
    else:
            print("is not a prime number",num)
else:
        print("is not prime number",num)
    

