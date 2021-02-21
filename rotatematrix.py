'''

For rotating matrix 90 clockwise

-----take transpose of matrix and call reverse on the rows of the matrix

For rotating matrix 90 anticlockwise

----- take transpose of matrix and call reverse on the columns.

for totating 180 anticlockwise :

    call reverse on rows and the call reverse on columns


'''


#########################
# Rotate matrix 90 degre anti clockwise again same as above

def reverseColumns(arr):
    for i in range(C):
        j = 0
        k = C-1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1


################################
# clockwise 90 ratation

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = len(matrix[0])
    column = len(matrix)

    for i in range(row):
        for j in range(i, column):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in matrix:
        i.reverse()
