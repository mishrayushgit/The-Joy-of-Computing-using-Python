def is_palindrome(string):
    if string[0] != string[-1]:
        return 0
    if len(string) <= 1:
        return 1 
    
    return is_palindrome(string[1:-1])
string = input()
print(is_palindrome(string))