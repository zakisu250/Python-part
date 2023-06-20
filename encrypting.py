message = input("Enter a message: ")
key = int(input("Enter key: "))
sec_mess = ""
for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26
        sec_mess += chr(char_code)
    else:
        sec_mess += char
print("Encrypted message: ", sec_mess)
