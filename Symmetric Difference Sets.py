from collections import Counter
from functools import reduce

# 4
# 2 4 5 9
# 4
# 2 4 11 12

m = 4  # int(input())
m_set = set(map(int, "2 4 5 9".split(" ")))
n = 4  # int(input())
n_set = set(map(int, "2 4 11 12".split(" ")))

print(*sorted(m_set.intersection(n_set), key=int), sep="\n")

# # solution #2
# a,b = [set(input().split()) for _ in range(4)][1::2]
# print(*sorted(a^b, key=int), sep='\n')

s1 = set()
s1.add("HackerRank")
print("s1:", s1)
s = set("HackerRank")
print(s)
s.add("H")
print(s)
print(s.add("HackerRank"))
print(s)

t = 7
my_set = set()
s = "7 UK China USA France NewZealand UK France "
print(s.split(" "))
for i in s.split(" ")[1:]:
    if i != "":
        if i == "NewZealand":
            lis = list(i)
            lis.insert(lis.index("Z"), " ")
            my_set.add("".join(lis))
        else:
            my_set.add(i.strip())

print("set:" + str(my_set))
print("size:", len(my_set))

word = "Hello"
counts = Counter(word)  # Counter({'l': 2, 'H': 1, 'e': 1, 'o': 1})
for i in sorted(set(word)):
    print(i, counts[i])

s12 = "NewZealand"
lis = list(s12)
lis.insert(lis.index("Z"), " ")
print("".join(lis))

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("set1:", set1)
set1.remove(2)
print("set1:", set1)
try:
    set1.remove(0)
except KeyError as e:
    print("Item: 0 is not in the list")
for _ in range(2):
    set1.pop()
    print("set1:", set1)

# 10
# 0 1 2 3 4 5 6 7 8 9
# 12
# remove 1
# pop
# pop
# discard 1
# discard 2
# remove 6
# pop
# discard 6
# discard 8
# discard 3
# discard 1
# discard 0

# output = 25
test_cases = 10
cases = set(map(int, "0 1 2 3 4 5 6 7 8 9".split(" ")))
cmd = ["remove 1", "pop", "pop", "discard 1", "discard 2", "remove 6", "pop", "discard 6", "discard 8", "discard 3",
       "discard 1", "discard 0", ]

for i in cmd:
    if "pop" in i:
        cases.pop()
    elif "remove" in i:
        cmd_type = i.split(" ")
        value = int(cmd_type[1])
        cases.remove(value)
    elif "discard" in i:
        cmd_type = i.split(" ")
        value = int(cmd_type[1])
        cases.discard(value)
sum = 0
for i in cases:
    sum += i
print(sum)

# 16
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
# 4
# intersection_update 10
# 2 3 5 6 8 9 1 4 7 11
# update 2
# 55 66
# symmetric_difference_update 5
# 22 7 35 62 58
# difference_update 7
# 11 22 35 55 58 62 66

print("CMD question about diff. starts here")


def print_set(set_type, set_value, cmd=None):
    print("set" + str(set_type), ":", set_value, (" cmd: " + str(cmd) if cmd is not None else ""))


t = 16
# t1 = set(map(int, input().split()))
# set2 = set(map(int, input().split()))

set12 = set(map(int, "1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52".split(" ")))

test_cases = 4
cmd = ["intersection_update 10 2 3 5 6 8 9 1 4 7 11", "update 2 55 66", "symmetric_difference_update 5 22 7 35 62 58",
       "difference_update 7 11 22 35 55 58 62 66"]

print("cmd:", cmd[3].split(" ")[0])
# print_set("start: ", 12, set12)
for i in cmd:
    # print("Before:")
    # print_set(12, set12)
    cmd_type = i.split(" ")
    if "intersection_update" == cmd_type[0]:
        cmd_type = i.split(" ")
        sub_test = cmd_type[1]
        set2 = set(map(int, cmd_type[2:]))
        set12.intersection_update(set2)
        # print_set(2, set2)
        # print_set(12, set12, cmd_type)
    elif "update" == cmd_type[0]:
        cmd_type = i.split(" ")
        sub_test = cmd_type[1]
        set2 = set(map(int, cmd_type[2:]))
        set12.update(set2)
        # print_set(2, set2)
        # print_set(12, set12, cmd_type)
    elif "symmetric_difference_update" == cmd_type[0]:
        cmd_type = i.split()
        sub_test = cmd_type[1]
        set2 = set(map(int, cmd_type[2:]))
        set12.symmetric_difference_update(set2)
        # print_set(2, set2)
        # print_set(12, set12, cmd_type)
    # elif "difference_update" in i:
    elif "difference_update" == cmd_type[0]:
        # print(i)
        cmd_type = i.split()
        sub_test = cmd_type[1]
        set2 = set(map(int, cmd_type[2:]))
        set12.difference_update(set2)
        # print("Difference: ", set12 - set2)
        # print_set(2, set2)
        # print_set(12, set12, cmd_type)

# print_set(12, set12)
print(sum(set12))

