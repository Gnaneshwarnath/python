rom={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
res=0
roman=input("Enter a Roman numeral: ")
for i in range(len(roman)):
    if i > 0 and rom[roman[i]] > rom[roman[i - 1]]:
        res+=rom[roman[i]] - 2 * rom[roman[i - 1]]
    else:
        res+=rom[roman[i]]
print("The integer value of is:", res)