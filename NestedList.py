def sortMarks(marks):
    return marks[1]


n = 5
# name = input("Enter name: ")
# score = input("Enter marks: ")
#   list = [[input("Enter name: "), input("Enter marks: ")] for _ in range(5)]

myList = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# print(myList)

myList.sort(key=lambda x: x[1])
# print(myList)
minMarks = myList[0][1]
myList = list(filter(lambda x: x[1] != minMarks, myList))
# print("list after removal")
# print(myList)
minMarks = myList[0][1]
print("MinaMarks: " + str(minMarks))
myList.sort(key=lambda x: x[0])

for i in myList:
    if minMarks in i:
        print(i[0])
list1 = [1, 2, 3, 4, 5, 6, 6, 7, 6, 6, 65]
print("Before: " + str(list1))
list1 = list(filter(lambda a: a != 6, list1))

print("After: " + str(list1))
