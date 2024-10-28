def check_char (para,n):
    for word in para:
        count = 0
        for i in range(len(para)):
            if word == para[i]:
                count+=1
        if count == n:
            return 1
    return 0
para = input().split()
n = int(input())
print(check_char(para,n))