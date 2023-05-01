import string

def rot13(message):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += string.ascii_uppercase[(string.ascii_uppercase.index(char) + 13) % 26]
            else:
                result += string.ascii_lowercase[(string.ascii_lowercase.index(char) + 13) % 26]
        else:
            result += char
    return result