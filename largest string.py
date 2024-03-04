str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
minimum=min(len(str1),len(str2))
largest=""
for i in range(minimum):
    if str1[i]==str2[i]:
        largest= largest+str1[i]
    else:
        break
print("Output:",largest)