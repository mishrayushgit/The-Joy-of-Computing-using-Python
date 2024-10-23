def find_kth_elements(listt,k):
    listt.sort()
    len_list= len(listt)
    kth_l = listt[-k]
    kth_s = listt[k-1]

    if kth_l == kth_s :
        mid = len_list//2
        if k == mid or k ==mid+1:
            return 1
        else:
            return -1
    else:
        return 0
lst = list(map(int, input().split()))
k = int(input())

# Find and print the result
result = find_kth_elements(lst, k)
print(result,end ="")
