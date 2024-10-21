def input_matrix (rows,columns):
    matrix = []
    rowlist = []
    for i in range (rows):
        for j in range (columns):
            rowlist.append(int(input(f"enter[{i}][{j}] element ")))
        matrix.append(rowlist)
        rowlist = []
    return matrix

def trans_matrix(matrix,columns,rows,const):
    trans_matrix =[]
    rowlist = []
    for i in range (columns):
        for j in range (rows):
            rowlist.append(matrix[j][i]*const)
        trans_matrix.append(rowlist)
        rowlist = []
        
    return trans_matrix

rows = int(input("enter the no. of rows "))
columns = int(input("enter the no. of columns "))
const = int(input("enter the constant "))

input_mat= input_matrix(rows,columns)
transposed_mat = trans_matrix(input_mat,columns,rows,const)
print (transposed_mat)
