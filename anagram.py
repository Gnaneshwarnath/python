strs = input("Enter the array of strings separated by spaces: ").split()
anagrams = {}

for word in strs:
    sorted_word = ''.join(sorted(word))
    if sorted_word in anagrams:
        anagrams[sorted_word].append(word)
    else:
        anagrams[sorted_word] = [word]

result = list(anagrams.values())

print("Grouped Anagrams:", result)
