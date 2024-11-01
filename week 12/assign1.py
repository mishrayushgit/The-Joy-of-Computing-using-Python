def collatz (number):
    if number == 1:
        return 0
    elif number % 2 == 0:
        number = number//2
    else :
        number = (number*3) + 1
    return collatz(number) + 1
input_no = int(input())
print(collatz(input_no))