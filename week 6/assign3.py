def non_decreasing(listt):
    if len(listt) <= 1:
        return True
    return listt[0]<=listt[1] and non_decreasing(listt[1:])
input = list(map(int,input().split()))
print(non_decreasing(input))