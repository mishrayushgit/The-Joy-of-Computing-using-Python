def multiply(no1,no2):
    if no2 == 0:
        return 0
    no2-=1
    return no1 + multiply(no1,no2)
input = list(map(int,input().split()))
print(multiply(input[0],input[1]))