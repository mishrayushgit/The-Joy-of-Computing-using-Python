a = [
    [1, 2, 3],
    [0, 5, 6],
    [0, 8, 9]
]
length_row = len(a[:])
length_col = len(a[0])
for i in range(length_row):
    min_row = min(a[i]) #finding the minimum in the row
    col_index = a[i].index(min_row)
    
    for j in range (length_row):
        saddle = 1
        if min_row < a[j][col_index]:
            saddle = 0
            break
    if saddle:
        print(min_row,"is the saddle point")
        
