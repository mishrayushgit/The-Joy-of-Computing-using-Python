def find_factors(numbers):
    check = min(numbers)
    count = 0
    factor_list =[]
    for i in range(1,check+1):
        for num in numbers:
            if num % i == 0:
                count +=1
        if len(numbers) == count:
            factor_list.append(str(i))
        count = 0
    print(" ".join(factor_list))
numbers = list(map(int,input().split(":")))
find_factors(numbers)
