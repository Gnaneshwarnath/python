import re
n=str(input("Enter the string: "))
n=n.replace(" ", "")
n=n.lower()
newstr = re.sub('[^A-Za-z]', '', n)
print(newstr)
if newstr == newstr[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
