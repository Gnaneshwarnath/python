word = input("Enter a word: ")

if word.isupper():
    print("Output: true")
elif word.islower():
    print("Output: true")
elif word[0].isupper() and word[1:].islower():
    print("Output: true")
else:
    print("Output: false")
