def log2 (number):
    if number == 1:
        return 0
    return 1 + log2(number//2)
number = int(input())
print(log2(number))