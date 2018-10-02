from collections import defaultdict
d = defaultdict(list)
list1 = []

n, m = map(int, input().split())

for i in range(0, n):
    d[input()].append(i+1)

for i in range(0, m):
    list1 = list1+[input()]

for i in list1:
    if i in d:
        print(" ".join( map(str, d[i])))
    else:
        print(-1)
print(d)
print(list1)
# input1 = list(map(int, input().split()))
# n, m = list(map(int, input().split()))
#
# dd1= defaultdict(list)
# # dd2 = defaultdict(list)
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)
#
# for i in range(n):
#     a = input()
#     dd1["A"].append(a)
#
# a_count = 0
#
# for i in range(m):
#     a = input()
#     dd1["B"].append(a)
#
# print("dd1:")
# for i in dd1.items():
#     print(i)
# # for i in dd2.items():
# #     print(i)
#
# test_list = dd1.get("B")
# # cases_list = dd1.get("A")
#
# print(test_list)
# print("cases:", dd1.get("A"), sep=" ")
#
# for i in test_list:
#     a_count = 0
#     for j in dd1.get("A"):
#         if i == j:
#             a_count += 1
#             print(i, dd1.get("A").index(i), sep=" ", end=" ")
#     print(a_count)
#
# for i in dd1.get("B"):
#     start = -1
#     while True:
#         try:
#             loc = dd1.get("A").index(i, start+1)
#             print(loc + 1, end=" ")
#             start = loc
#         except ValueError:
#             break
#     print()
#
#
