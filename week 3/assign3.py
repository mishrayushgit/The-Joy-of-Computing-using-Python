# Create a Python program that takes a list of integers, reverses the list, adds the values at odd indices from both the original and reversed lists, and creates a new list with the result. The new list should be printed in the end.
def oddlist(numbers):
    numbers1 = numbers[:]
    numbers1.reverse()
    final_list = []
    for i in range(len(numbers)): 
        if i%2 != 0 :
            total = numbers[i] + numbers1[i]
            final_list.append(total)
        else :
            final_list.append(numbers[i])
    final_list = ' '.join(map(str,final_list))
    return final_list
numbers = input()
numbers = list(map(int,numbers.split()))
print(oddlist(numbers),end ="")
