# Create a Python program that removes all duplicate positive integer numbers(includes zero) from a list and prints the unique numbers in the order they first appeared.The program should prompt the user to input a list of numbers, then process the list to remove duplicates and print the resulting list of unique numbers.
def remove_duplicates(no_list):
    occured = []
    for i in no_list:
        if i not in occured:
            occured.append(i)
    occured = ' '.join(map(str, occured))
    return occured

numbers = input()
numbers = list(map(int,numbers.split()))
print(remove_duplicates(numbers),end = "")
