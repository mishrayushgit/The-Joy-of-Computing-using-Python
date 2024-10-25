def tuple_sum (n,tuple):
    sum = 0
    for i in range(n*2):
        if i % 2 == 0:
            sum+=tuple[i]
    return sum 

n = int(input())
my_tuple = ()
for _ in range(n):
    my_tuple =  my_tuple + tuple(map(int,input().split()))
print(tuple_sum(n,my_tuple))
    