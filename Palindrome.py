word = input("Please enter a string: ")

#Reverse the word & combine the letters in reversed order
new_word = "".join(reversed(word))
print(new_word)

if word == new_word:
    print(word, " is a palindrome!")
else:
    print(word, " is not a palindrome!")