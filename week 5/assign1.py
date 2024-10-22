def input_list():
    no_list = input("enter the no's in ascending order: ")
    no_list = list(map(int,no_list.split()))
    return no_list
def binary_search(no_list,number):
    list_len = len(no_list)
    low = 0
    high = len(no_list)-1
    flag = 0
    while low <= high:
        mid = (high + low)//2
        if no_list[mid] == number :
            print(no_list.index(no_list[mid]))
            flag = 1
            break
        elif no_list[mid] > number :
            high = mid - 1
        elif no_list[mid] < number :
            low = mid + 1
    if not flag:
        print(-1)
def main():
    no_list = input_list()
    number = int(input("enter the number from the list: "))
    binary_search(no_list,number)
main()