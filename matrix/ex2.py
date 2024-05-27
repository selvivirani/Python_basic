k = [[2,3 ,4],
     [7,8,9],
     [2,1,4]]
n= [[1,7.6],
    [6,4,2],
    [4,6,2]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(k)):
    for j in range(len(k[0])):
        result[i][j] = k[i][j] + n[i][j]
for r in result:
  print(r)

