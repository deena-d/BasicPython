matrix1 = [[1, 1, 1],
[1, 1, 1],
[1, 1, 1]]
matrix2 = [[2, 2, 2],
[2, 2, 2],
[2, 2, 2]]
rmatrix = [[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]
for i in range(0,len(matrix1)):
for j in range(0,len(matrix2)):
rmatrix[i][j] = matrix1[i][j] + matrix2[i][j]
for r in rmatrix:
print(r)
