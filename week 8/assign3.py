def highest(listt,k):
    largest = 0
    for i in range(len(listt)):
        listt[i] = listt[i]*k
    listt.sort()
    return listt[len(listt)-1]
listt = list(map(int,input().split()))
k = int(input())
print(highest(listt,k))