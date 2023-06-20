word = input("Enter the word to hide in uppercase: ")
secret = ""
for char in word:
    secret += str(ord(char) - 23)
print("Secret code: ", secret)
normstr = ""
for i in range(0, len(secret)-1, 2):
    chars = secret[i] + secret[i+1]
    normstr += chr(int(chars) + 23)
print("Word: ", normstr)
