list = [[2,3,4],[7,77,34],[2,0,1],[6,7,2]]

print("the original list:-" + str(list))

res = {list[0][ele] : list[ele +1] for ele in range (len(list) - 1)}

print("the assigned  matrix:" + str (res))

