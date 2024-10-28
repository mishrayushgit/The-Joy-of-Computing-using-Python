def heavyside (num_list):
    middle = len(num_list)//2
    left_side,right_side = 0,0
    for i in range(middle):
        left_side += num_list[i]
        right_side += num_list[-(i+1)]
    if left_side>right_side:
        return -1
    elif right_side>left_side:
        return 1
    else:
        return 0
num_list = list(map(int,input().split()))
print(heavyside(num_list))