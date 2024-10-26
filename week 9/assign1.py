def count_vowels(string):
    count = 0
    vowels =["a","e","i","o","u"]
    string = string.lower()
    for i in range(len(string)):
        if string[i] in vowels:
            count+=1
    print(count)
string = input()
count_vowels(string)

