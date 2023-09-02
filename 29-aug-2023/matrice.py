#https://github.com/BhatiaUday/cp-sem1/
matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[9,8,7], [6,5,4], [3,2,1]]


rowsA = len(matrix1)
colsA = len(matrix1[0])
rowsB = len(matrix2)
colsB = len(matrix2[0])
if colsA != rowsB:
    print("Cannot Multiply!")
else:
    result = [[0 for row in range(colsB)] for col in range(rowsA)]
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
for r in result:
    print(r)