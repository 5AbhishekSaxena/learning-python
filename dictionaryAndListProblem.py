import math
# Harsh 25 26.5 28
# Anurag 26 28 30
# Harsh
from functools import reduce

n = 2
student_marks = {}
line2 = ["Harsh 25 26.5 28", "Anurag 26 28 30"]
for _ in range(n):
    for i in range(n):
        line = line2[i].split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
query_name = "Harsh"

for i in student_marks["Harsh"]:
    print(i)
# avg = 0.0
query_scores = student_marks[query_name]
print("Scores: ", query_scores)
avg = reduce(lambda x, y: x+y, query_scores)/len(query_scores)
print("Lambda avg: ", avg)
ssum = 0
for i in query_scores:
    ssum += i
    avg = ssum/(len(query_scores))

print(avg)

myList = {"1": {"Name": "Harsh", "Age": 20, "School": "Ryan International School", "Category": "General", "phone number": 8447919879},
          "2": {"Name": "Ram", "Age": 30, "Scores": [30, 40, 12]}}

for i in myList:
    print(i)

key = "Scores"
for i in myList:
    if key in myList[i]:
        for j in myList[i][key]:
            print(j)
    else:
        print("Invalid Key!!!")
print(math.sin(30))
