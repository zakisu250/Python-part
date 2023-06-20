orig_word = input("Enter the word: ")
orig_word = orig_word.upper()
list_of_words = orig_word.split()
for word in list_of_words:
    print(word[0], end="")
print()
