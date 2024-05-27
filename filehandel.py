with open("selvi.txt","r") as f:
    data = f.read()
    print(data)

with open("selvi.txt","r") as f:
    data = f.read(10)
    print(data)
 

with open  ("selvi.txt","w") as f:
    data = f.write("this is python")
    print(data)


#append
with open  ("selvi.txt","a") as f:
    data = f.write("\ni am using python")
    print(data)


#seek mode
with open("selvi.txt","r") as f:
    f.seek(4)
print(f.read())