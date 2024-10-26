def average_lenght(string):
    str_list = string.split()
    lenght = 0
    for i in str_list:
        lenght += len(i)
    avg = float(lenght/2)
    if avg > 4:
        print(1)
    else :
        print(0)
string = input()
average_lenght(string)