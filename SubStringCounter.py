import string

str = "ABCDCDCDCD"  # input("Enter a string: ")
subString = "CDCD"  # input("Enter the substring: ")

i = 0
count = 0

while i < len(str):
    if str.find(subString, i) >= 0:
        i = str.find(subString, i) + 1
        count += 1
    else:
        break

print(count)

s = "chris alan"    # input("Enter a string: ")
print(string.capwords(s, " "))
