def list(newlist):
    size = len(newlist)
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1]= temp
    return newlist 
newlist = [12 , 7 ,77 ,23]
print(list(newlist))