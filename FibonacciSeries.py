a = 0
b = 1
i = 0

n = int(input("Enter number of terms: "))

print(a)
print(b)

while i < n-2:
    sum = a + b
    print(str(sum) + " ")
    a = b
    b = sum
    i += 1
