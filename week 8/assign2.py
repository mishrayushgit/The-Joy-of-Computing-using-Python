def check_anagram(string1,string2):
    string1 = string1.lower()
    string2 = string2.lower()
    for i in range(len(string1)):
        if 97 <= ord(string1[i]) <= 122 :
            if string1[i] not in string2:
                return 0
    return 1
string1 = input()
string2 = input()
print(check_anagram(string1,string2))