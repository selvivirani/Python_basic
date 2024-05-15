# def squer():
#  ran = []
# for i in range(5):
#     num = int(input("enter number:-".format(i +1)))
#     ran.append(num) 
# sum_squer=sum(x**2 for x in ran)
# return sum_squer
# print("sum squears:-", squer())

num = int(input())
num1 = {i : i**2 for i in range(1,num+1)}
print(num1)