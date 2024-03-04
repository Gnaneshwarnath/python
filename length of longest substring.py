s = input("Enter a string: ")

max_length = 0
current_length = 0
visited_chars = set()

for char in s:
    if char in visited_chars:
        visited_chars.clear()
        current_length = 0
    visited_chars.add(char)
    current_length += 1
    max_length = max(max_length, current_length)

print("Length of the longest substring without repeating characters:", max_length)
