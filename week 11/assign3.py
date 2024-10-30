mapping = {
    'a': '0', 'k': '1', 'x': '2', 'y': '3',
    's': '4', 'm': '5', 'b': '6', 'd': '7',
    'p': '8', 'z': '9'
}
def decode_date(encoded_date):
    decoded_date = ""
    for char in encoded_date:
        if char in mapping:
            decoded_date += mapping[char]
        else:
            decoded_date += char
    print(decoded_date)
encoded_data = input()
decode_date(encoded_data)