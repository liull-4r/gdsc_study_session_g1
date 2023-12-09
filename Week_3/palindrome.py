word = input("Enter a word: ")
word = word.replace(" ", "").lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")