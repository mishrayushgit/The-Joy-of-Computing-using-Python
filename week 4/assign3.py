def input_matrix (rows,columns):
    matrix = []
    rowlist = []
    for i in range (rows):
        for j in range (columns):
            rowlist.append(int(input(f"enter[{i}][{j}] element ")))
        matrix.append(rowlist)
        rowlist = []
    return matrix
def trans_matrix(matrix,rows,columns):
    trans_matrix =[]
    rowlist = []
    for i in range (columns):
        for j in range (rows):
            rowlist.append(matrix[j][i])
        trans_matrix.append(rowlist)
        rowlist = []
        
    return trans_matrix
def negative_matrix(matrix,rows,columns):
    neg_matrix =[]
    rowlist = []
    for i in range (rows):
        for j in range (columns):
            rowlist.append(matrix[i][j]*(-1))
        neg_matrix.append(rowlist)
        rowlist = []
    return neg_matrix
def test_skew(negative,trans,rows,columns):
    flag = 1
    for i in range (rows):
        for j in range (columns):
            if negative[i][j] != trans[i][j]:
                flag = 0
    return flag
                
def main ():
    dimension = int(input("Enter dimension of a square matrix "))
    columns = dimension
    rows = dimension
    matrix = input_matrix(rows,columns)
    transpose = trans_matrix(matrix,rows,columns)
    negative = negative_matrix(matrix,rows,columns)
    flag = 1
    for i in range (rows):
        for j in range (columns):
            if negative[i][j] != transpose[i][j]:
                flag = 0
    
    print(flag)
    
main()