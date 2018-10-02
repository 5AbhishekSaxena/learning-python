# import math
# # n = int(input("Enter a number: "))
# # while n > 0:
# #     print("Hello", sep="\n", end=" ")
# #     print("n:", n, end="\n")
# #     n = n - 1
# #     if n == 3:
# #         break
# # print(n)
#
# # while True:
# #     line = input("> ")
# #     if line == "done" or line == "Done":
# #         break
# #     elif line[0] == "#":
# #         continue
# #     print(line)
# # print("Done!")
#
# for i in ["abc", "bcd", "def", "ghi", "jkl", "mno"]:
#     print("Happy New Year", i, end="!\n")
# print("Done!")
#
# max_number = 0
# min_number = None
# found = False
# for i in [1, 20, 3, 4, 5]:
#
#     if min_number is None:
#         min_number = i
#     elif min_number >= i:
#         min_number = i
#
#     if i >= max_number:
#         max_number = i
#
#     if i == 2:
#         found = True
#         break
#
# print("Max Number: ", max_number)
# print("Min. Number: ", min_number)
# print("isThere: ", found)
#
# dic = {"x": 50, "y": 3}
# key = "x"
# if key in dic:
#     print(dic[key])
#
# l = [1, 2, 3, 4]
# for i in range(len(l)):
#     print(i)
#
# str = "Hello There"
# for i in str:
#     # letter = str[i]
#     print(i, end="")
#
# print()
# print("loc: ", "helllo".find("h"))
#
# data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# atpos = data.find("@")
# print(atpos)
# sposs = data.find(" ", atpos)
# print(data[atpos:sposs])
#
# # content = dir(math)
# # print(content)
#
# inputfile = open("text.txt", "r")
#
# for i in inputfile:
#     print(i)
#
# inputfile.close()
# outputfile = open("text.txt", "a")
# outputfile.write("\nHey this is added")
# outputfile.close()
#

# num = None
# try:
#     num = input("Enter Number: ")
#     num = int(num)
#     print("number:", num * 2)
# except ValueError:
#     print("Invalid Input: %s" % num)

list_of_lists = []
for i in range(3):
    L = []
    for j in range(4):
        L.append(i*j)
    list_of_lists.append(L)

print(list_of_lists)


list1 = [(1, 2, 3), (2, 3, 4)]
count = 1
for i in list1:
    print("count: ", count)
    for j in i:
        print(j, end=" ")
    count = count + 1
    print()