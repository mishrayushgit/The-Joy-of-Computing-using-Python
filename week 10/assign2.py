def long_tail(num_list):
    count = 0
    for flo in num_list:
        flo_list = flo.split(".")
        if len(flo_list[0]) < len(flo_list[1]):
            count+=1
    return(count)
num_list = list(map(str,input().split()))
print(long_tail(num_list))