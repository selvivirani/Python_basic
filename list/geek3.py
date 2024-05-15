def position(list,pos1,pos2):
    list[pos1],list[pos2] = list[pos2], list[pos1]
    return list
list = [23 ,77 ,7 ,67]
pos1 ,pos2 = 1,3
print(position(list,pos1-1,pos2-1))
