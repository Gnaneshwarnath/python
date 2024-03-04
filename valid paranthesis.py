# Taking user input
s = input("Enter a string with parentheses: ")
stack = []
mapping = {')': '(', '}': '{', ']': '['}

for char in s:
    if char in mapping:
        top_element = stack.pop() if stack else '#'
        if mapping[char] != top_element:
            print("Invalid parentheses")
            break
    else:
        stack.append(char)

else:
    # If the loop completes without breaking, the parentheses are valid
    print("Valid parentheses")
