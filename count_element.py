from collections import Counter


# Input: 5 4 7 5 4 6 7 1 2 54 4 7 6 1
list1 = list(map(int, input().split()))
count = Counter(list1)

for i in count:
    # if count[i] == 1:
    print(i, count[i])

# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))
