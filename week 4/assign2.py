rows = int(input("enter the no. of rows"))
columns = int(input("enter the no. of columns"))
const = int(input("enter the constant"))
matrix = []
rowlist = []
for i in range (rows):
    for j in range (columns):
        rowlist.append(int(input(f"enter[{i}][{j}] element ")))
    matrix.append(rowlist)
    rowlist = []
