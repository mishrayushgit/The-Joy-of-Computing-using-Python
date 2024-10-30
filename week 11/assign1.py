def alter_format(input_date):
    temp = input_date[0]
    input_date[0] = input_date[1]
    input_date[1]= temp
    year = input_date[2]
    input_date[2] = year[-2:]
    return "-".join(input_date)
input_date = input().split("/")
print(alter_format(input_date))