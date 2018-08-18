from collections import Counter
k = int(input())
list1 = list(map(int, input().split()))
count = Counter(list1)

for i in count:
    if count[i] == 1:
        print(i)

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))