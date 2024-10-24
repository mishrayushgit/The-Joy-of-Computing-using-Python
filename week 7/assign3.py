def input_matrix (rows):
    matrix = []
    rowlist = []
    for i in range (rows):
        rowlist = list(map(int,input().split()))
        matrix.append(rowlist)
        rowlist = []
    return matrix
def check_symmetric_binary(matrix,columns,rows):
    final_output=""
    is_binary = 1
    trans_matrix =[]
    rowlist = []
    for i in range (rows):
        for j in range (columns):
            if not (0<=matrix[i][j]<=1):
                is_binary = 0
                break
    if is_binary:
        final_output +="1"
    else:
        final_output+="0"
    for i in range (columns):
        for j in range (rows):
            rowlist.append(matrix[j][i])
        trans_matrix.append(rowlist)
        rowlist = []
    if matrix == trans_matrix:
        final_output +="1"
    else:
        final_output +="0"
    return final_output
r = int(input())
c = int(input())
matrix = input_matrix(r)
print(check_symmetric_binary(matrix,c,r))