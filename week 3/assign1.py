# Create a Python program that finds the second largest number in a list of positive integers(includes zero). The program should prompt the user to input a list of numbers, then compute and print the second largest number in that list.
def second_largest(numbers):
    numbers = set(numbers)
    numbers.remove(max(numbers))
    return max(numbers)

numbers = input()
numbers = list(map(int,numbers.split()))
print(second_largest(numbers),end ="")